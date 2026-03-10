from mcp.server.fastmcp import FastMCP
from lib.http import get, post, extract_data


def register(mcp: FastMCP):

    @mcp.tool()
    async def get_community_list() -> str:
        """获取所有支持的开源社区列表。适用于 PPT 中展示社区全景图，或作为其他查询的前置步骤。"""
        result = await post("/community/list")
        if result.get("code") != 1:
            return f"API 错误：{result.get('message', '未知错误')}"
        data = result.get("data", [])
        lines = [f"共 {len(data)} 个社区："]
        for c in data:
            lines.append(f"  - {c}")
        return "\n".join(lines)

    @mcp.tool()
    async def get_metric_dict() -> str:
        """获取指标字典，包含所有可用指标的名称、中文名、单位和定义。适用于 PPT 数据说明页。"""
        result = await get("/dict/metric")
        if result.get("code") != 1:
            return f"API 错误：{result.get('message', '未知错误')}"
        data = extract_data(result)
        if not data:
            return "暂无指标数据"
        lines = ["指标字典："]
        for m in data:
            lines.append(f"  [{m.get('name')}] {m.get('name_zh')} — 说明：{m.get('definition')} — 适用范围：{m.get('areasofuse_zh')}")
        return "\n".join(lines)
