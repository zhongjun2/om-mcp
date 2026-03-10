"""自定义响应格式化函数，用于处理复杂的 API 响应结构"""
from typing import Any, Dict


def format_community_contribute(data: Any, call_params: Dict[str, Any]) -> str:
    """格式化社区贡献历史数据（按月序列）"""
    community = call_params.get("community", "")

    if not data:
        return f"社区 {community} 暂无贡献指标数据"

    lines = [f"社区贡献指标：{community}", ""]

    if isinstance(data, dict):
        for k, v in data.items():
            lines.append(f"  - {k}：{v}")
    else:
        lines.append(str(data))

    return "\n".join(lines)


def format_ci_metrics(data: Any, call_params: Dict[str, Any]) -> str:
    """格式化 CI 指标数据（总运行次数、成功/失败/待处理数、成功率、平均时长及趋势）"""
    if not data:
        return "暂无 CI 指标数据"

    lines = ["CI 指标统计："]

    # 处理聚合统计
    if isinstance(data, dict):
        if "total_runs" in data:
            lines.append(f"  总运行次数：{data.get('total_runs', 'N/A')}")
        if "success_count" in data:
            lines.append(f"  成功次数：{data.get('success_count', 'N/A')}")
        if "failure_count" in data:
            lines.append(f"  失败次数：{data.get('failure_count', 'N/A')}")
        if "pending_count" in data:
            lines.append(f"  待处理次数：{data.get('pending_count', 'N/A')}")
        if "success_rate" in data:
            lines.append(f"  成功率：{data.get('success_rate', 'N/A')}%")
        if "avg_duration" in data:
            lines.append(f"  平均时长：{data.get('avg_duration', 'N/A')}")

        # 处理趋势数据
        if "trend" in data and isinstance(data["trend"], list):
            lines.append("\n  趋势数据：")
            for item in data["trend"]:
                lines.append(f"    {item.get('date', 'N/A')}: {item.get('count', 'N/A')} 次")

    return "\n".join(lines)


def format_community_health(data: Any, call_params: Dict[str, Any]) -> str:
    """格式化社区健康度数据（12 个维度，1-5 分制）"""
    if not data:
        return "暂无健康度数据"

    # 指标标签映射
    METRIC_LABELS = {
        "nss":                    "社区影响力(NSS)",
        "download":               "下载量",
        "issue_close":            "Issue关闭率",
        "certification":          "认证",
        "first_response":         "首次响应",
        "leverage_ratio":         "杠杆率",
        "tech_influence":         "技术影响力",
        "version_release":        "版本发布",
        "elephant_coefficient":   "大象系数",
        "effective_maintenance":  "有效维护",
        "contribution_diversity": "贡献多样性",
        "contributor_interaction":"贡献者互动",
    }

    community = call_params.get("community", "")
    avg = data.get("avg_score", "N/A")

    lines = [
        f"社区：{community}",
        f"数据日期：{data.get('created_at', 'N/A')}",
        f"综合健康度评分：{avg} / 5.0",
        "",
        "各指标评分（1-5分）及原始值：",
    ]

    for key, label in METRIC_LABELS.items():
        score = data.get(key, "-")
        raw = data.get(f"{key}_value", "-")
        lines.append(f"  - {label}：{score} 分（原始值：{raw}）")

    return "\n".join(lines)
