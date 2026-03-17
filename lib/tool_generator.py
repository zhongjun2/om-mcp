"""动态生成 MCP 工具函数并注册到 FastMCP 实例"""
import inspect
from typing import List
from mcp.server.fastmcp import FastMCP
from lib.template_loader import ToolTemplate
from lib.http import get, post, extract_data
from lib.response_formatter import format_response
from tools.health import COMMUNITY_MAP


def generate_all_tools(mcp: FastMCP, templates: List[ToolTemplate]):
    """根据模板列表生成并注册所有工具"""
    for template in templates:
        tool_func = _make_tool_function(template)
        mcp.tool()(tool_func)


def _make_tool_function(template: ToolTemplate):
    """根据模板创建异步工具函数"""

    # 构建函数签名
    sig = _build_signature(template)

    async def tool_fn(**kwargs):
        # 1. COMMUNITY_MAP 归一化
        normalized_params = {}
        for param_def in template.params:
            value = kwargs.get(param_def.name, param_def.default)

            if param_def.community_map and value:
                key = str(value).strip().lower()
                mapped = COMMUNITY_MAP.get(key)
                if not mapped:
                    available = ", ".join(sorted(COMMUNITY_MAP.keys()))
                    return f"未找到社区 '{value}'，可用社区（小写）：{available}"
                value = mapped.lower()

            normalized_params[param_def.name] = value

        # 2. 构建 URL 路径（path_params）
        url_path = template.http_path
        for path_param in template.path_params:
            param_value = normalized_params.get(path_param, "")
            url_path = url_path.replace(f"{{{path_param}}}", str(param_value))

        # 3. 构建 body/query 参数
        body_params = {}
        query_params = {}

        # 添加常量参数
        if template.constant_params:
            if template.http_method == "post":
                body_params.update(template.constant_params)
            else:
                query_params.update(template.constant_params)

        # 添加动态参数
        for param_def in template.params:
            value = normalized_params[param_def.name]

            # 跳过 path 参数（已在 URL 中）
            if param_def.in_ == "path":
                continue

            # conditional 逻辑：非空才加入
            if param_def.conditional:
                if param_def.type == "str" and not value:
                    continue
                if param_def.type == "int" and value == 0:
                    continue

            # 使用 body_key 别名
            target_key = param_def.body_key

            if param_def.in_ == "body":
                body_params[target_key] = value
            elif param_def.in_ == "query":
                query_params[target_key] = value

        # 4. 调用 HTTP 方法
        if template.http_method == "post":
            result = await post(url_path, body_params if body_params else None)
        else:
            result = await get(url_path, params=query_params if query_params else None)

        # 5. 错误检查
        if result.get("code") != 1:
            return f"API 错误：{result.get('message', '未知错误')}"

        # 6. 提取数据
        if template.use_extract_data:
            data = extract_data(result)
        else:
            data = result.get("data")

        # 7. 格式化响应
        return format_response(
            data,
            template.response_config,
            normalized_params,
            template.empty_data_message
        )

    # 设置函数元数据
    tool_fn.__name__ = template.name
    tool_fn.__signature__ = sig
    tool_fn.__doc__ = _build_docstring(template)

    return tool_fn


def _build_signature(template: ToolTemplate) -> inspect.Signature:
    """构建函数签名（FastMCP 用它发现参数类型）"""
    parameters = []

    for param_def in template.params:
        # 类型映射
        if param_def.type == "int":
            annotation = int
        else:
            annotation = str

        # 默认值
        if param_def.required:
            default = inspect.Parameter.empty
        else:
            default = param_def.default

        parameters.append(
            inspect.Parameter(
                param_def.name,
                inspect.Parameter.KEYWORD_ONLY,
                default=default,
                annotation=annotation
            )
        )

    return inspect.Signature(
        parameters=parameters,
        return_annotation=str
    )


def _build_docstring(template: ToolTemplate) -> str:
    """构建函数文档字符串"""
    lines = [template.description]

    if template.params:
        lines.append("")
        lines.append("Args:")
        for param_def in template.params:
            req_str = "（必填）" if param_def.required else "（可选）"
            lines.append(f"    {param_def.name}: {param_def.description}{req_str}")

    return "\n".join(lines)
