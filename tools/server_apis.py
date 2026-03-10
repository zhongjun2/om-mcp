import json
from datetime import datetime
from mcp.server.fastmcp import FastMCP
from lib.http import get, post, extract_data


def _date_to_ms(date_str: str) -> int:
    dt = datetime.strptime(date_str.strip(), "%Y-%m-%d")
    return int(dt.timestamp() * 1000)


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

    @mcp.tool()
    async def get_project_hotspot() -> str:
        """获取最近更新的热点仓库列表（按更新时间倒序前10个）。适用于 PPT 展示社区近期热点动态。"""
        now = datetime.utcnow()
        body = {
            "start": int(now.replace(year=now.year - 1).timestamp() * 1000),
            "end": int(now.timestamp() * 1000),
        }
        result = await post("/project/hotspot", body)
        if result.get("code") != 1:
            return f"API 错误：{result.get('message', '未知错误')}"
        data = extract_data(result)
        if not data:
            return "暂无热点仓库数据"
        lines = [f"热点仓库 Top {len(data)}："]
        for i, repo in enumerate(data, 1):
            lines.append(f"  {i}. {repo.get('repo_name')} — 更新于 {repo.get('updated_at')} — {repo.get('html_url', '')}")
        return "\n".join(lines)

    @mcp.tool()
    async def get_project_repo_list() -> str:
        """获取仓库列表（最近更新的 50 个）。适用于 PPT 展示社区仓库规模总览。"""
        now = datetime.utcnow()
        body = {
            "start": int(now.replace(year=now.year - 1).timestamp() * 1000),
            "end": int(now.timestamp() * 1000),
        }
        result = await post("/project/repolist", body)
        if result.get("code") != 1:
            return f"API 错误：{result.get('message', '未知错误')}"
        data = extract_data(result)
        if not data:
            return "暂无仓库数据"
        lines = [f"仓库列表（共 {len(data)} 个）："]
        for repo in data:
            lines.append(f"  - {repo.get('repo_name')} | 创建：{repo.get('created_at')} | 更新：{repo.get('updated_at')}")
        return "\n".join(lines)

    @mcp.tool()
    async def get_project_active() -> str:
        """获取活跃仓库统计（总仓库数、活跃数、非活跃数）。适用于 PPT 展示社区整体活跃情况。"""
        now = datetime.utcnow()
        body = {
            "start": int(now.replace(year=now.year - 1).timestamp() * 1000),
            "end": int(now.timestamp() * 1000),
        }
        result = await post("/project/active", body)
        if result.get("code") != 1:
            return f"API 错误：{result.get('message', '未知错误')}"
        data = extract_data(result)
        if not data:
            return "暂无活跃项目数据"
        return (
            f"仓库活跃统计：\n"
            f"  总仓库数：{data.get('total_repos', 'N/A')}\n"
            f"  活跃仓库：{data.get('active_repos', 'N/A')}\n"
            f"  非活跃仓库：{data.get('inactive_repos', 'N/A')}"
        )

    @mcp.tool()
    async def get_project_topn_company_pr(community: str = "", start_time: str = "", end_time: str = "") -> str:
        """获取 PR 贡献企业 Top N 排名（贡献数量和占比）。适用于 PPT 展示企业贡献分布饼图/条形图数据。

        Args:
            community: 社区名称（可选）
            start_time: 开始时间，格式 YYYY-MM-DD（可选）
            end_time: 结束时间，格式 YYYY-MM-DD（可选）
        """
        now = datetime.utcnow()
        body = {
            "start": _date_to_ms(start_time) if start_time else int(now.replace(year=now.year - 1).timestamp() * 1000),
            "end": _date_to_ms(end_time) if end_time else int(now.timestamp() * 1000),
            "event": "pr",
            "metric": "company",
            "orgList": [],
            "private": "false",
            "community": community.lower() if community else "",
        }

        result = await post("/query/contributes/topn/total", body)
        if result.get("code") != 1:
            return f"API 错误：{result.get('message', '未知错误')}"
        data = extract_data(result)
        if not data:
            return "暂无企业 PR 贡献数据"
        items = data if isinstance(data, list) else data.get("list", [])
        lines = ["企业 PR 贡献 Top 排名："]
        for i, item in enumerate(items, 1):
            rank = item.get("row_num", i)
            company = item.get("company", "N/A")
            count = item.get("pr_total", 0)
            lines.append(f"  {rank}. {company} — {count} 个 PR")
        return "\n".join(lines)

    @mcp.tool()
    async def get_company_count(community: str = "", start_time: str = "", end_time: str = "") -> str:
        """获取社区参与的组织/企业数量统计。

        Args:
            community: 社区名称（可选）
            start_time: 开始时间，格式 YYYY-MM-DD（可选）
            end_time: 结束时间，格式 YYYY-MM-DD（可选）
        """
        now = datetime.utcnow()
        body = {
            "start": _date_to_ms(start_time) if start_time else int(now.replace(year=now.year - 1).timestamp() * 1000),
            "end": _date_to_ms(end_time) if end_time else int(now.timestamp() * 1000),
            "source": "",
            "internal": "",
            "pageNum": 1,
            "pageSize": 1,
            "community": community.lower() if community else "",
        }

        result = await post("/query/company/detail", body)
        if result.get("code") != 1:
            return f"API 错误：{result.get('message', '未知错误')}"
        data = extract_data(result)
        if not data:
            return "暂无组织数据"

        total = data.get("total_count", "N/A") if isinstance(data, dict) else "N/A"
        return f"参与贡献的组织/企业总数：{total}"

    @mcp.tool()
    async def get_project_topn_user_pr() -> str:
        """获取 PR 贡献个人开发者 Top N 排名。适用于 PPT 展示个人贡献者排行榜。"""
        result = await post("/project/topn/user/pr")
        if result.get("code") != 1:
            return f"API 错误：{result.get('message', '未知错误')}"
        data = extract_data(result)
        if not data:
            return "暂无用户 PR 贡献数据"
        lines = ["开发者 PR 贡献 Top 排名："]
        for i, item in enumerate(data, 1):
            lines.append(f"  {i}. {item.get('name')}（{item.get('user')}）— {item.get('count')} 个 PR — 所属：{item.get('company')}")
        return "\n".join(lines)
