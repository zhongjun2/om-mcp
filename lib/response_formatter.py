"""响应格式化模块，根据模板配置将 API 响应转换为人类可读的字符串"""
from typing import Any, Dict
import importlib


def format_response(data: Any, response_config: Dict[str, Any], call_params: Dict[str, Any], empty_message: str) -> str:
    """根据响应配置格式化数据

    Args:
        data: API 返回的数据（已提取）
        response_config: 响应配置字典
        call_params: 调用参数（用于模板渲染）
        empty_message: 数据为空时的消息
    """
    if not data:
        return empty_message

    response_type = response_config.get("type", "scalar")

    if response_type == "custom":
        return _format_custom(data, response_config, call_params)
    elif response_type == "scalar":
        return _format_scalar(data, response_config, call_params)
    elif response_type == "list":
        return _format_list(data, response_config, call_params)
    elif response_type == "paginated_list":
        return _format_paginated_list(data, response_config, call_params)
    elif response_type == "branching":
        return _format_branching(data, response_config, call_params)
    else:
        return str(data)


def _format_custom(data: Any, config: Dict[str, Any], call_params: Dict[str, Any]) -> str:
    """调用自定义格式化函数"""
    formatter_name = config.get("formatter")
    if not formatter_name:
        return str(data)

    try:
        # 动态导入 tools.custom_formatters 模块
        module = importlib.import_module("tools.custom_formatters")
        formatter_func = getattr(module, formatter_name)
        return formatter_func(data, call_params)
    except (ImportError, AttributeError) as e:
        return f"格式化错误：找不到函数 {formatter_name} ({e})"


def _format_scalar(data: Any, config: Dict[str, Any], call_params: Dict[str, Any]) -> str:
    """格式化单个对象（键值对展示）"""
    if not isinstance(data, dict):
        return str(data)

    lines = []
    header = config.get("header", "")
    if header:
        lines.append(header)

    fields = config.get("fields", [])
    for field in fields:
        label = field.get("label", "")
        key = field.get("key", "")
        suffix = field.get("suffix", "")
        value = data.get(key, "N/A")
        lines.append(f"  {label}：{value}{suffix}")

    return "\n".join(lines)


def _format_list(data: Any, config: Dict[str, Any], call_params: Dict[str, Any]) -> str:
    """格式化数组（逐项展示）"""
    if not isinstance(data, list):
        return str(data)

    lines = []

    # 渲染头部模板
    header_template = config.get("header_template", "")
    if header_template:
        context = {"count": len(data), **call_params}
        lines.append(header_template.format_map(context))

    # 应用字段转换
    transforms = config.get("field_transforms", {})
    transformed_data = []
    for item in data:
        if isinstance(item, dict):
            new_item = item.copy()
            for new_key, transform_def in transforms.items():
                source_key = transform_def.get("source", "")
                transform_type = transform_def.get("transform", "")
                if source_key in item:
                    new_item[new_key] = _apply_transform(item[source_key], transform_type)
            transformed_data.append(new_item)
        else:
            transformed_data.append(item)

    # 渲染每一项
    item_template = config.get("item_template", "")
    for i, item in enumerate(transformed_data, 1):
        if isinstance(item, dict):
            context = {"index": i, **item, **call_params}
            lines.append(item_template.format_map(context))
        else:
            lines.append(f"  {i}. {item}")

    return "\n".join(lines)


def _format_paginated_list(data: Any, config: Dict[str, Any], call_params: Dict[str, Any]) -> str:
    """格式化分页列表"""
    if not isinstance(data, dict):
        return str(data)

    list_key = config.get("list_key", "list")
    total_key = config.get("total_key", "total")

    items = data.get(list_key, [])
    total = data.get(total_key, 0)

    lines = []

    # 渲染头部
    header_template = config.get("header_template", "")
    if header_template:
        context = {
            "page": call_params.get("page", 1),
            "total": total,
            "count": len(items),
            **call_params
        }
        lines.append(header_template.format_map(context))

    # 渲染每一项
    item_template = config.get("item_template", "")
    for i, item in enumerate(items, 1):
        if isinstance(item, dict):
            context = {"index": i, **item, **call_params}
            lines.append(item_template.format_map(context))
        else:
            lines.append(f"  {i}. {item}")

    return "\n".join(lines)


def _format_branching(data: Any, config: Dict[str, Any], call_params: Dict[str, Any]) -> str:
    """根据参数值分支格式化"""
    branch_on = config.get("branch_on", "")
    branch_condition = config.get("branch_condition", "non_empty")

    # 检查分支条件
    param_value = call_params.get(branch_on, "")
    should_branch = False

    if branch_condition == "non_empty":
        should_branch = bool(param_value)
    elif branch_condition == "non_zero":
        should_branch = param_value != 0

    # 选择配置
    if should_branch and isinstance(data, list):
        branch_config = config.get("branched", {})
    else:
        branch_config = config.get("default", {})

    # 递归调用对应的格式化函数
    branch_type = branch_config.get("type", "scalar")
    if branch_type == "scalar":
        return _format_scalar(data, branch_config, call_params)
    elif branch_type == "list":
        return _format_list(data, branch_config, call_params)
    else:
        return str(data)


def _apply_transform(value: Any, transform_type: str) -> Any:
    """应用字段转换"""
    if transform_type == "date_prefix":
        # 截取 ISO 日期前 10 位
        if isinstance(value, str) and len(value) >= 10:
            return value[:10]
    return value
