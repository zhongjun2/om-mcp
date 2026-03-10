# OM-MCP 接口列表

本文档记录所有已实现的 MCP 工具接口。

## 社区相关 (4个)

### get_community_health
查询指定社区的健康度指标数据。

**参数：**
- `community` (str): 社区名称，如 openEuler、MindSpore 等
- `date` (str, 可选): 查询日期，格式 YYYY-MM-DD

**返回：** 综合评分及各子指标分数

---

### list_communities
列出所有支持查询的社区名称。

**参数：** 无

**返回：** 社区名称列表

---

### get_community_list
获取所有支持的开源社区列表。

**参数：** 无

**返回：** 社区详细信息列表

---

### get_company_count
获取社区参与的组织/企业数量统计。

**参数：**
- `community` (str, 可选): 社区名称
- `start_time` (str, 可选): 开始时间，格式 YYYY-MM-DD
- `end_time` (str, 可选): 结束时间，格式 YYYY-MM-DD

**返回：** 参与企业数量

---

## 项目/仓库 (5个)

### get_project_hotspot
获取最近更新的热点仓库列表（按更新时间倒序前10个）。

**参数：** 无

**返回：** 热点仓库列表

---

### get_project_repo_list
获取仓库列表（最近更新的 50 个）。

**参数：** 无

**返回：** 仓库列表

---

### get_project_active
获取活跃仓库统计（总仓库数、活跃数、非活跃数）。

**参数：** 无

**返回：** 仓库活跃统计

---

### get_project_topn_company_pr
获取 PR 贡献企业 Top N 排名（贡献数量和占比）。

**参数：**
- `community` (str, 可选): 社区名称
- `start_time` (str, 可选): 开始时间，格式 YYYY-MM-DD
- `end_time` (str, 可选): 结束时间，格式 YYYY-MM-DD

**返回：** 企业 PR 贡献排名

---

### get_project_topn_user_pr
获取 PR 贡献个人开发者 Top N 排名。

**参数：** 无

**返回：** 个人开发者 PR 贡献排名

---

## Issue (6个)

### get_issues_aggregate
获取 Issue 聚合统计：总数、开启数、关闭数、首次响应时长、关闭时长、关闭率。

**参数：**
- `community` (str, 可选): 社区名称
- `start_time` (str, 可选): 开始时间，格式 YYYY-MM-DD
- `end_time` (str, 可选): 结束时间，格式 YYYY-MM-DD
- `interval` (str, 可选): 时间粒度，支持 day/week/month

**返回：** Issue 聚合统计数据

---

### get_issues_by_sig
获取各 SIG（兴趣组）的 Issue 分布统计。

**参数：**
- `community` (str, 可选): 社区名称
- `start_time` (str, 可选): 开始时间，格式 YYYY-MM-DD
- `end_time` (str, 可选): 结束时间，格式 YYYY-MM-DD

**返回：** 各 SIG 的 Issue 分布

---

### get_issues_agg_page
获取 Issue 汇总分页统计，支持按仓库/SIG/命名空间等维度分组。

**参数：**
- `community` (str, 可选): 社区名称
- `start_date` (str, 可选): 开始日期，格式 YYYY-MM-DD
- `end_date` (str, 可选): 结束日期，格式 YYYY-MM-DD
- `group_dim` (str, 可选): 分组维度，如 repo/sig/namespace，默认 repo
- `namespace` (str, 可选): 命名空间筛选
- `repo_path` (str, 可选): 仓库路径筛选
- `issue_type` (str, 可选): Issue 类型筛选
- `source` (str, 可选): 来源平台
- `private` (str, 可选): 是否私仓，true/false
- `asc` (str, 可选): 升序字段
- `desc` (str, 可选): 降序字段

**返回：** Issue 汇总分页数据

---

### get_issues_agg_sig
获取 Issue SIG 维度汇总统计。

**参数：**
- `community` (str, 可选): 社区名称
- `start_date` (str, 可选): 开始日期，格式 YYYY-MM-DD
- `end_date` (str, 可选): 结束日期，格式 YYYY-MM-DD
- `sig_name` (str, 可选): SIG 名称筛选
- `issue_type` (str, 可选): Issue 类型
- `source` (str, 可选): 来源平台
- `desc` (str, 可选): 降序字段

**返回：** SIG 维度 Issue 统计

---

### get_issues_detail
获取 Issue 详情分页列表。

**参数：**
- `community` (str, 可选): 社区名称
- `start_date` (str, 可选): 开始日期，格式 YYYY-MM-DD
- `end_date` (str, 可选): 结束日期，格式 YYYY-MM-DD
- `namespace` (str, 可选): 命名空间
- `repo_path` (str, 可选): 仓库路径
- `title` (str, 可选): 标题关键字
- `state` (str, 可选): 状态 open/closed
- `issue_type` (str, 可选): Issue 类型
- `priority` (str, 可选): 优先级
- `page_num` (int, 可选): 页码，默认 1
- `page_size` (int, 可选): 每页数量，默认 20

**返回：** Issue 详情列表

---

### get_issue_ref_pr
获取 Issue 关联 PR 信息。

**参数：**
- `community` (str, 可选): 社区名称
- `start_date` (str, 可选): 开始日期，格式 YYYY-MM-DD
- `end_date` (str, 可选): 结束日期，格式 YYYY-MM-DD
- `namespace` (str, 可选): 命名空间
- `repo_path` (str, 可选): 仓库路径
- `sig_group` (str, 可选): SIG 组
- `pr_state` (str, 可选): PR 状态 open/merged/closed
- `issue_state` (str, 可选): Issue 状态 open/closed
- `pr_number` (str, 可选): PR 编号
- `issue_number` (str, 可选): Issue 编号

**返回：** Issue 和 PR 的关联关系

---

## PR (5个)

### get_prs_aggregate
获取 PR 聚合统计：总数、开启数、关闭数、合并数、首次响应时长、合并率等。

**参数：**
- `community` (str, 可选): 社区名称
- `start_time` (str, 可选): 开始时间，格式 YYYY-MM-DD
- `end_time` (str, 可选): 结束时间，格式 YYYY-MM-DD
- `interval` (str, 可选): 时间粒度，支持 day/week/month

**返回：** PR 聚合统计数据

---

### get_prs_by_sig
获取各 SIG 的 PR 分布统计。

**参数：**
- `community` (str, 可选): 社区名称
- `start_time` (str, 可选): 开始时间，格式 YYYY-MM-DD
- `end_time` (str, 可选): 结束时间，格式 YYYY-MM-DD

**返回：** 各 SIG 的 PR 分布

---

### get_prs_agg_page
获取 PR 汇总分页统计，支持按仓库/SIG/命名空间等维度分组。

**参数：**
- `community` (str, 可选): 社区名称
- `start_date` (str, 可选): 开始日期，格式 YYYY-MM-DD
- `end_date` (str, 可选): 结束日期，格式 YYYY-MM-DD
- `group_dim` (str, 可选): 分组维度，如 repo/sig/namespace，默认 repo
- `namespace` (str, 可选): 命名空间筛选
- `repo` (str, 可选): 仓库名称
- `pr_type` (str, 可选): PR 类型
- `private` (str, 可选): 是否私仓，true/false
- `desc` (str, 可选): 降序字段

**返回：** PR 汇总分页数据

---

### get_prs_detail
获取 PR 详情分页列表。

**参数：**
- `community` (str, 可选): 社区名称
- `start_date` (str, 可选): 开始日期，格式 YYYY-MM-DD
- `end_date` (str, 可选): 结束日期，格式 YYYY-MM-DD
- `namespace` (str, 可选): 命名空间
- `repo_path` (str, 可选): 仓库路径
- `title` (str, 可选): 标题关键字
- `state` (str, 可选): 状态 open/merged/closed
- `page_num` (int, 可选): 页码，默认 1
- `page_size` (int, 可选): 每页数量，默认 20

**返回：** PR 详情列表

---

### get_repo_user_list
获取仓库活跃用户分页列表。

**参数：**
- `community` (str, 可选): 社区名称
- `page` (int, 可选): 页码，默认 1
- `page_size` (int, 可选): 每页数量，默认 10

**返回：** 活跃用户列表

---

## CI (1个)

### get_ci_metrics
获取项目 CI（持续集成）指标。

**参数：**
- `community` (str, 可选): 社区名称
- `start_time` (str, 可选): 开始时间，格式 YYYY-MM-DD
- `end_time` (str, 可选): 结束时间，格式 YYYY-MM-DD

**返回：** CI 运行次数、成功率、平均时长等

---

## 论坛 (3个)

### get_forum_agg
获取论坛帖子汇总分页统计。

**参数：**
- `community` (str, 可选): 社区名称
- `start_date` (str, 可选): 开始日期，格式 YYYY-MM-DD
- `end_date` (str, 可选): 结束日期，格式 YYYY-MM-DD
- `namespace` (str, 可选): 命名空间
- `repo_path` (str, 可选): 仓库路径
- `title` (str, 可选): 标题关键字
- `state` (str, 可选): 状态筛选
- `page_num` (int, 可选): 页码，默认 1
- `page_size` (int, 可选): 每页数量，默认 20
- `desc` (str, 可选): 降序排列字段，默认 open_count

**返回：** 论坛帖子汇总数据

---

### get_forum_tag_agg
获取论坛标签维度汇总统计。

**参数：**
- `community` (str, 可选): 社区名称
- `start_date` (str, 可选): 开始日期，格式 YYYY-MM-DD
- `end_date` (str, 可选): 结束日期，格式 YYYY-MM-DD
- `category_name` (str, 可选): 分类名称
- `tag_name` (str, 可选): 标签名称
- `group_dim` (str, 可选): 分组维度
- `desc` (str, 可选): 降序字段

**返回：** 标签维度统计数据

---

### get_forum_detail
获取论坛帖子详情分页列表。

**参数：**
- `community` (str, 可选): 社区名称
- `start_date` (str, 可选): 开始日期，格式 YYYY-MM-DD
- `end_date` (str, 可选): 结束日期，格式 YYYY-MM-DD
- `title` (str, 可选): 标题关键字
- `desc` (str, 可选): 降序字段，默认 created_at

**返回：** 帖子详情列表

---

## SIG (1个)

### get_sig_leverage_ratio
获取 SIG 撬动比（外部贡献占比）统计。

**参数：**
- `community` (str, 可选): 社区名称
- `start_date` (str, 可选): 开始日期，格式 YYYY-MM-DD
- `end_date` (str, 可选): 结束日期，格式 YYYY-MM-DD
- `source` (str, 可选): 来源平台
- `sig_list` (str, 可选): 逗号分隔的 SIG 名称列表

**返回：** SIG 撬动比数据

---

## 用户 (2个)

### get_users_page
获取开发者汇总分页列表。

**参数：**
- `community` (str, 可选): 社区名称
- `start_date` (str, 可选): 开始日期，格式 YYYY-MM-DD
- `end_date` (str, 可选): 结束日期，格式 YYYY-MM-DD
- `page_num` (int, 可选): 页码，默认 1
- `page_size` (int, 可选): 每页数量，默认 20

**返回：** 开发者列表

---

### get_users_trend
获取开发者趋势统计（按时间段统计开发者数量变化）。

**参数：**
- `community` (str, 可选): 社区名称
- `start_date` (str, 可选): 开始日期，格式 YYYY-MM-DD
- `end_date` (str, 可选): 结束日期，格式 YYYY-MM-DD
- `interval` (str, 可选): 时间粒度，day/week/month，默认 month
- `metric` (str, 可选): 统计维度
- `event_list` (str, 可选): 逗号分隔的事件类型列表
- `org_list` (str, 可选): 逗号分隔的组织列表

**返回：** 开发者趋势数据

---

## 服务平台 (2个)

### get_source_total
获取论坛/邮件/会议等服务平台汇总数据。

**参数：**
- `community` (str, 可选): 社区名称
- `start_date` (str, 可选): 开始日期，格式 YYYY-MM-DD
- `end_date` (str, 可选): 结束日期，格式 YYYY-MM-DD
- `source` (str, 可选): 来源平台，如 forum/email/meeting
- `group_dim` (str, 可选): 分组维度
- `namespace` (str, 可选): 命名空间
- `private` (str, 可选): 是否私仓，true/false
- `desc` (str, 可选): 降序字段，默认 open_count

**返回：** 服务平台汇总数据

---

### get_source_trend
获取论坛/邮件/会议等服务平台趋势数据。

**参数：**
- `community` (str, 可选): 社区名称
- `start_date` (str, 可选): 开始日期，格式 YYYY-MM-DD
- `end_date` (str, 可选): 结束日期，格式 YYYY-MM-DD
- `source` (str, 可选): 来源平台，如 forum/email/meeting
- `interval` (str, 可选): 时间粒度，day/week/month，默认 month
- `metrics` (str, 可选): 指标类型

**返回：** 服务平台趋势数据

---

## 注册用户 (1个)

### get_regist_user_detail
获取注册用户详情分页列表。

**参数：**
- `community` (str, 可选): 社区名称
- `start_date` (str, 可选): 开始日期，格式 YYYY-MM-DD
- `end_date` (str, 可选): 结束日期，格式 YYYY-MM-DD
- `source` (str, 可选): 来源平台
- `company` (str, 可选): 企业名称筛选
- `internal` (str, 可选): 内外部标识
- `page_num` (int, 可选): 页码，默认 1
- `page_size` (int, 可选): 每页数量，默认 20

**返回：** 注册用户详情列表

---

## 组织/企业 (2个)

### get_company_detail
获取参与社区的组织/企业详情分页列表。

**参数：**
- `community` (str, 可选): 社区名称
- `start_date` (str, 可选): 开始日期，格式 YYYY-MM-DD
- `end_date` (str, 可选): 结束日期，格式 YYYY-MM-DD
- `source` (str, 可选): 来源平台
- `internal` (str, 可选): 内外部标识
- `page_num` (int, 可选): 页码，默认 1
- `page_size` (int, 可选): 每页数量，默认 20

**返回：** 企业详情列表

---

### get_company_trend
获取组织/企业参与趋势数据。

**参数：**
- `community` (str, 可选): 社区名称
- `start_date` (str, 可选): 开始日期，格式 YYYY-MM-DD
- `end_date` (str, 可选): 结束日期，格式 YYYY-MM-DD
- `source` (str, 可选): 来源平台
- `company` (str, 可选): 企业名称
- `internal` (str, 可选): 内外部标识
- `interval` (str, 可选): 时间粒度，day/week/month，默认 month

**返回：** 企业参与趋势数据

---

## 贡献 (4个)

### get_contributes_topn
获取贡献 TopN 汇总排名，支持按组织/仓库/SIG/开发者维度统计。

**参数：**
- `community` (str, 可选): 社区名称
- `start_date` (str, 可选): 开始日期，格式 YYYY-MM-DD
- `end_date` (str, 可选): 结束日期，格式 YYYY-MM-DD
- `event` (str, 可选): 贡献类型，pr/issue/comment/addcode，默认 pr
- `metric` (str, 可选): 统计维度，company_type/company/sig/repo/user，默认 company_type
- `topn` (int, 可选): TopN 数量，默认 10
- `private` (str, 可选): 是否包含私仓，true/false，默认 false
- `org_list` (str, 可选): 逗号分隔的命名空间/组织列表

**返回：** 贡献 TopN 排名

---

### get_contributes_topn_item
获取贡献 TopN 明细（某维度值的时间序列数据）。

**参数：**
- `community` (str, 可选): 社区名称
- `start_date` (str, 可选): 开始日期，格式 YYYY-MM-DD
- `end_date` (str, 可选): 结束日期，格式 YYYY-MM-DD
- `event` (str, 可选): 贡献类型，pr/issue/comment/addcode，默认 pr
- `metric` (str, 可选): 统计维度，repo/sig/company，默认 repo
- `metric_val` (str, 可选): 维度值，如仓库名或 SIG 名
- `interval` (str, 可选): 时间粒度，day/week/month，默认 month
- `source` (str, 可选): 来源平台
- `private` (str, 可选): 是否包含私仓，true/false，默认 false

**返回：** TopN 明细时间序列数据

---

### get_contributes_page
获取贡献汇总分页列表（按组织/仓库等聚合）。

**参数：**
- `community` (str, 可选): 社区名称
- `start_date` (str, 可选): 开始日期，格式 YYYY-MM-DD
- `end_date` (str, 可选): 结束日期，格式 YYYY-MM-DD
- `metric` (str, 可选): 统计维度
- `source` (str, 可选): 来源平台
- `private` (str, 可选): 是否私仓
- `internal` (str, 可选): 内外部标识
- `org_list` (str, 可选): 逗号分隔的组织列表
- `page_num` (int, 可选): 页码，默认 1
- `page_size` (int, 可选): 每页数量，默认 20
- `desc` (str, 可选): 降序字段，默认 pr_total

**返回：** 贡献汇总分页数据

---

### get_contributes_trend
获取贡献趋势统计（按时间段统计各类贡献数量）。

**参数：**
- `community` (str, 可选): 社区名称
- `start_date` (str, 可选): 开始日期，格式 YYYY-MM-DD
- `end_date` (str, 可选): 结束日期，格式 YYYY-MM-DD
- `interval` (str, 可选): 时间粒度，day/week/month，默认 month
- `metric` (str, 可选): 统计维度
- `event_list` (str, 可选): 逗号分隔的贡献类型列表，默认 pr
- `org_list` (str, 可选): 逗号分隔的组织列表

**返回：** 贡献趋势数据

---

## 其他 (2个)

### get_metric_dict
获取指标字典，包含所有可用指标的名称、中文名、单位和定义。

**参数：** 无

**返回：** 指标字典

---

### get_filter_options
获取社区数据筛选条件（如 SIG 列表、仓库列表、标签等）。

**参数：**
- `community` (str, 可选): 社区名称
- `tab` (str, 可选): 标签页标识，如 issue/pr/repo 等

**返回：** 筛选条件选项

---

### get_account_trend
获取社区账号注册趋势数据。

**参数：**
- `community` (str, 可选): 社区名称
- `tab` (str, 可选): 标签页标识

**返回：** 账号注册趋势数据

---

## 更新记录

- 2026-03-10: 删除 get_cla_user_list、get_cla_trend（HTTP 404）；lib/http.py 改用标准 logging
