from datetime import datetime
from mcp.server.fastmcp import FastMCP
from lib.http import post, extract_data


def _date_to_ms(date_str: str) -> int:
    dt = datetime.strptime(date_str.strip(), "%Y-%m-%d")
    return int(dt.timestamp() * 1000)


def register(mcp: FastMCP):

    @mcp.tool()
    async def get_issues_aggregate(community: str = "", start_time: str = "", end_time: str = "", interval: str = "") -> str:
        """获取 Issue 聚合统计：总数、开启数、关闭数、首次响应时长、关闭时长、关闭率。
        适用于 PPT 展示社区 Issue 处理能力概览。

        Args:
            community: 社区名称（可选），如 openEuler、MindSpore、CANN 等
            start_time: 开始时间，格式 YYYY-MM-DD（可选）
            end_time: 结束时间，格式 YYYY-MM-DD（可选）
            interval: 时间粒度（可选），支持 day/week/month，用于按时间段统计
        """
        now = datetime.utcnow()
        body = {
            "start": _date_to_ms(start_time) if start_time else int(now.replace(year=now.year - 1).timestamp() * 1000),
            "end": _date_to_ms(end_time) if end_time else int(now.timestamp() * 1000),
            "group_dim": "sub_community",
            "issue_type": "",
            "issue_type_list": [],
            "namespace": "",
            "repo_path": "",
            "source": "",
            "internalList": [],
            "private": "false",
            "asc": "one_day_response_ratio",
            "desc": "",
        }
        if community:
            body["community"] = community.lower()
        if interval:
            body["interval"] = interval

        result = await post("/query/issues/agg", body)
        if result.get("code") != 1:
            return f"API 错误：{result.get('message', '未知错误')}"
        data = extract_data(result)
        if not data:
            return "暂无 Issue 聚合数据"

        # 如果是按时间段统计，返回列表数据
        if interval and isinstance(data, list):
            lines = [f"Issue 按{interval}统计（共 {len(data)} 个时间段）："]
            for item in data:
                lines.append(
                    f"  {item.get('time_bucket', 'N/A')}: "
                    f"总数 {item.get('count', 0)}, "
                    f"关闭 {item.get('closed_count', 0)}, "
                    f"关闭率 {item.get('closed_ratio', 'N/A')}"
                )
            return "\n".join(lines)

        # 否则返回聚合数据（从 list[0] 提取）
        item = data.get('list', [{}])[0] if isinstance(data, dict) else {}
        return (
            f"Issue 聚合统计：\n"
            f"  总数：{item.get('count', 'N/A')}\n"
            f"  开启中：{item.get('open_count', 'N/A')}\n"
            f"  已关闭：{item.get('closed_count', 'N/A')}\n"
            f"  关闭率：{item.get('closed_ratio', 'N/A')}\n"
            f"  平均首次响应时长：{item.get('avg_first_reply_time', 'N/A')} 天\n"
            f"  平均关闭时长：{item.get('avg_closed_time', 'N/A')} 天"
        )

    @mcp.tool()
    async def get_issues_by_sig(community: str = "", start_time: str = "", end_time: str = "") -> str:
        """获取各 SIG（兴趣组）的 Issue 分布统计，包括每个 SIG 的 Issue 数量、关闭率等。
        适用于 PPT 中按 SIG 展示 Issue 分布图表。

        Args:
            community: 社区名称（可选）
            start_time: 开始时间，格式 YYYY-MM-DD（可选）
            end_time: 结束时间，格式 YYYY-MM-DD（可选）
        """
        now = datetime.utcnow()
        body = {
            "start": _date_to_ms(start_time) if start_time else int(now.replace(year=now.year - 1).timestamp() * 1000),
            "end": _date_to_ms(end_time) if end_time else int(now.timestamp() * 1000),
            "group_dim": "sig",
            "issue_type": "",
            "issue_type_list": [],
            "namespace": "",
            "sig_name": "",
            "sig_name_list": [],
            "source": "",
            "internalList": [],
            "private": "false",
            "asc": "",
            "desc": "count",
        }
        if community:
            body["community"] = community.lower()

        result = await post("/query/issues/agg/sig", body)
        if result.get("code") != 1:
            return f"API 错误：{result.get('message', '未知错误')}"
        data = extract_data(result)
        if not data:
            return "暂无 SIG Issue 数据"
        sig_list = data.get("list", []) if isinstance(data, dict) else []
        total = data.get("total_count", len(sig_list)) if isinstance(data, dict) else len(sig_list)
        lines = [f"各 SIG Issue 统计（共 {total} 个 SIG）："]
        for item in sig_list:
            lines.append(
                f"  [{item.get('sig_name')}] 总数 {item.get('count')}，开启 {item.get('open_count')}，"
                f"关闭率 {item.get('closed_ratio')}，平均响应 {item.get('avg_first_reply_time')} 天"
            )
        return "\n".join(lines)

    @mcp.tool()
    async def get_prs_aggregate(community: str = "", start_time: str = "", end_time: str = "", interval: str = "") -> str:
        """获取 PR 聚合统计：总数、开启数、关闭数、合并数、首次响应时长、合并率等。
        适用于 PPT 展示社区代码贡献活跃度概览。

        Args:
            community: 社区名称（可选）
            start_time: 开始时间，格式 YYYY-MM-DD（可选）
            end_time: 结束时间，格式 YYYY-MM-DD（可选）
            interval: 时间粒度（可选），支持 day/week/month，用于按时间段统计
        """
        now = datetime.utcnow()
        body = {
            "start": _date_to_ms(start_time) if start_time else int(now.replace(year=now.year - 1).timestamp() * 1000),
            "end": _date_to_ms(end_time) if end_time else int(now.timestamp() * 1000),
            "group_dim": "",
            "pr_type": "",
            "namespace": "",
            "repo": "",
            "private": "false",
            "asc": "",
            "desc": "",
        }
        if community:
            body["community"] = community.lower()
        if interval:
            body["interval"] = interval

        result = await post("/query/prs/agg", body)
        if result.get("code") != 1:
            return f"API 错误：{result.get('message', '未知错误')}"
        data = extract_data(result)
        if not data:
            return "暂无 PR 聚合数据"

        # 如果是按时间段统计，返回列表数据
        if interval and isinstance(data, list):
            lines = [f"PR 按{interval}统计（共 {len(data)} 个时间段）："]
            for item in data:
                lines.append(
                    f"  {item.get('time_bucket', 'N/A')}: "
                    f"总数 {item.get('count', 0)}, "
                    f"合并 {item.get('merged_count', 0)}, "
                    f"合并率 {item.get('merged_ratio', 'N/A')}"
                )
            return "\n".join(lines)

        # 否则从 list[0] 提取聚合数据
        item = data.get('list', [{}])[0] if isinstance(data, dict) else {}
        return (
            f"PR 聚合统计：\n"
            f"  总数：{item.get('count', 'N/A')}\n"
            f"  开启中：{item.get('open_count', 'N/A')}\n"
            f"  已关闭：{item.get('closed_count', 'N/A')}\n"
            f"  已合并：{item.get('merged_count', 'N/A')}\n"
            f"  关闭率：{item.get('closed_ratio', 'N/A')}\n"
            f"  合并率：{item.get('merged_ratio', 'N/A')}\n"
            f"  平均首次响应时长：{item.get('avg_first_reply_time', 'N/A')} 天\n"
            f"  平均关闭时长：{item.get('avg_closed_time', 'N/A')} 天"
        )

    @mcp.tool()
    async def get_prs_by_sig(community: str = "", start_time: str = "", end_time: str = "") -> str:
        """获取各 SIG 的 PR 分布统计，包括每个 SIG 的 PR 数量、合并率等。
        适用于 PPT 按 SIG 展示代码贡献分布图。

        Args:
            community: 社区名称（可选）
            start_time: 开始时间，格式 YYYY-MM-DD（可选）
            end_time: 结束时间，格式 YYYY-MM-DD（可选）
        """
        now = datetime.utcnow()
        body = {
            "start": _date_to_ms(start_time) if start_time else int(now.replace(year=now.year - 1).timestamp() * 1000),
            "end": _date_to_ms(end_time) if end_time else int(now.timestamp() * 1000),
            "group_dim": "sig",
            "pr_type": "",
            "namespace": "",
            "sig_name": "",
            "private": "false",
            "asc": "",
            "desc": "",
        }
        if community:
            body["community"] = community.lower()

        result = await post("/query/prs/agg/sig", body)
        if result.get("code") != 1:
            return f"API 错误：{result.get('message', '未知错误')}"
        data = extract_data(result)
        if not data:
            return "暂无 SIG PR 数据"
        sig_list = data.get("list", []) if isinstance(data, dict) else []
        total = data.get("total_count", len(sig_list)) if isinstance(data, dict) else len(sig_list)
        lines = [f"各 SIG PR 统计（共 {total} 个 SIG）："]
        for item in sig_list:
            lines.append(
                f"  [{item.get('sig_name')}] 总数 {item.get('count')}，开启 {item.get('open_count')}，"
                f"关闭率 {item.get('closed_ratio')}，合并率 {item.get('merged_ratio', 'N/A')}，"
                f"平均响应 {item.get('avg_first_reply_time')} 天"
            )
        return "\n".join(lines)

    @mcp.tool()
    async def get_repo_user_list(community: str = "", page: int = 1, page_size: int = 10) -> str:
        """获取仓库活跃用户分页列表，包含每位用户的 PR、Issue、评论数量。
        适用于 PPT 展示社区活跃贡献者排行。

        Args:
            community: 社区名称（可选）
            page: 页码，默认 1
            page_size: 每页数量，默认 10
        """
        now = datetime.utcnow()
        body = {
            "start": int(now.replace(year=now.year - 1).timestamp() * 1000),
            "end": int(now.timestamp() * 1000),
            "namespace": "",
            "repo_path": "",
            "private": "false",
            "asc": "",
            "desc": "in_user_count",
            "pageNum": page,
            "pageSize": page_size,
        }
        if community:
            body["community"] = community.lower()

        result = await post("/query/repo/user/page", body)
        if result.get("code") != 1:
            return f"API 错误：{result.get('message', '未知错误')}"
        data = extract_data(result)
        if not data:
            return "暂无用户数据"
        user_list = data.get("list", []) if isinstance(data, dict) else []
        total = data.get("total", len(user_list)) if isinstance(data, dict) else len(user_list)
        lines = [f"活跃用户列表（第 {page} 页，共 {total} 人）："]
        for u in user_list:
            lines.append(
                f"  {u.get('user_name')}（{u.get('user_login')}）— PR {u.get('pr_count')}，"
                f"Issue {u.get('issue_count')}，评论 {u.get('comment_count')}，"
                f"最近活跃：{u.get('last_active_time')}"
            )
        return "\n".join(lines)
