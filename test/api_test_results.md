# MCP 接口测试结果

测试时间：2026-03-10
测试社区：openEuler（除特殊说明外）

说明：
- ✅ 通过：接口正常返回数据
- ⚠️ 部分：接口返回但数据存在问题
- ❌ 失败：接口返回错误

---

## 社区相关

### get_community_health ✅
**测试问题**：openEuler 社区 2026-03-01 的健康度如何？
**调用参数**：community=openEuler, date=2026-03-01
**返回结果**：
```
社区：openeuler
数据日期：2026-03-01
综合健康度评分：4.24 / 5.0

各指标评分（1-5分）及原始值：
  - 社区影响力(NSS)：5 分（原始值：0.69）
  - 下载量：5 分（原始值：6308471）
  - Issue关闭率：3 分（原始值：0.7651163）
  - 认证：4 分（原始值：5）
  - 首次响应：5 分（原始值：0.78729165）
  - 杠杆率：5 分（原始值：2.5136857）
  - 技术影响力：4 分（原始值：562.0）
  - 版本发布：5 分（原始值：0.0）
  - 大象系数：4 分（原始值：4）
  - 有效维护：5 分（原始值：0.93181366）
  - 贡献多样性：5 分（原始值：63）
  - 贡献者互动：1 分（原始值：1.0）
```

---

### list_communities ✅
**测试问题**：列出所有支持查询的社区
**调用参数**：无
**返回结果**：
```
支持查询的社区列表（共 23 个）：
ascendnpuir, boostkit, cann, cannopen, mindcluster, mindie,
mindseriessdk, mindspeed, mindspore, mindstudio, openeuler,
openfuyao, opengauss, opensource, openubmc, pta, pytorch,
sgl, tilelang, triton, unifiedbus, verl, vllm
```

---

### get_community_list ✅
**测试问题**：获取所有社区列表
**调用参数**：无
**返回结果**：共 23 个社区（含 openEuler、openGauss、MindSpore 等）

---

### get_company_count ❌
**测试问题**：openEuler 社区 2026 年 Q1 参与的企业数量是多少？
**调用参数**：community=openEuler, start_time=2026-01-01, end_time=2026-03-10
**返回结果**：`API 错误：系统内部出现错误`

---

## 项目/仓库

### get_project_hotspot ❌
**测试问题**：获取最近更新的热点仓库
**调用参数**：无
**返回结果**：`API 错误：系统内部出现错误`

---

### get_project_repo_list ❌
**测试问题**：获取仓库列表
**调用参数**：无
**返回结果**：`API 错误：系统内部出现错误`

---

### get_project_active ❌
**测试问题**：获取活跃仓库统计
**调用参数**：无
**返回结果**：`API 错误：系统内部出现错误`

---

### get_project_topn_company_pr ❌
**测试问题**：openEuler 社区 2026 年 Q1 PR 贡献企业 Top N 排名
**调用参数**：community=openEuler, start_time=2026-01-01, end_time=2026-03-10
**返回结果**：`API 错误：系统内部出现错误`

---

### get_project_topn_user_pr ❌
**测试问题**：获取 PR 贡献个人开发者 Top N 排名
**调用参数**：无
**返回结果**：`API 错误：系统内部出现错误`

---

## Issue

### get_issues_aggregate ✅
**测试问题**：openEuler 社区 2026 年 Q1 的 Issue 统计情况
**调用参数**：community=openEuler, start_time=2026-01-01, end_time=2026-03-10
**返回结果**：
```
Issue 聚合统计：
  总数：4477
  开启中：2434
  已关闭：3309
  关闭率：0.4563
  平均首次响应时长：15.82 天
  平均关闭时长：20.57 天
```

---

### get_issues_by_sig ❌
**测试问题**：openEuler 社区各 SIG 的 Issue 分布情况
**调用参数**：community=openEuler, start_time=2026-01-01, end_time=2026-03-10
**返回结果**：`API 错误：系统内部出现错误`

---

### get_issues_agg_page ✅
**测试问题**：openEuler 社区按仓库维度的 Issue 汇总统计
**调用参数**：community=openEuler, group_dim=repo
**返回结果**：共 12010 条记录，返回前 10 条仓库 Issue 统计（含 aalib 等）

---

### get_issues_agg_sig ❌
**测试问题**：openEuler 社区 SIG 维度 Issue 汇总
**调用参数**：community=openEuler
**返回结果**：`API 错误：系统内部出现错误`

---

### get_issues_detail ✅
**测试问题**：查看 openEuler 社区最近的 Issue 详情
**调用参数**：community=openEuler, page_num=1, page_size=3
**返回结果**：
```
Issue 详情（共 24297 条，8099 页）：
  #N/A [closed] CVE-2025-26597 — 2026-03-09 15:18:04
  #N/A [closed] 缺少对空补丁的判断逻辑 — 2026-03-09 16:28:27
  #N/A [closed] CVE-2026-0988 — 2026-03-05 21:44:19
```

---

### get_issue_ref_pr ✅
**测试问题**：查看 openEuler 社区 Issue 和 PR 的关联关系
**调用参数**：community=openEuler
**返回结果**：共 171952 条记录，返回前 10 条关联关系（含 llvm-project、abichecker 等仓库）

---

## PR

### get_prs_aggregate ✅
**测试问题**：openEuler 社区 2026 年 Q1 的 PR 总数是多少？
**调用参数**：community=openEuler, start_time=2026-01-01, end_time=2026-03-10
**返回结果**：
```
PR 聚合统计：
  总数：16171
  开启中：1708
  已关闭：2505
  已合并：12398
  关闭率：0.8944
  平均首次响应时长：3.47 天
  平均关闭时长：4.42 天
```

---

### get_prs_by_sig ❌
**测试问题**：openEuler 社区各 SIG 的 PR 分布情况
**调用参数**：community=openEuler, start_time=2026-01-01, end_time=2026-03-10
**返回结果**：`API 错误：系统内部出现错误`

---

### get_prs_agg_page ✅
**测试问题**：openEuler 社区按仓库维度的 PR 汇总统计
**调用参数**：community=openEuler, group_dim=repo
**返回结果**：
```
PR 汇总（按 repo 分组）（共 12090 条，1209 页）：
  [kernel] 开启 1064，平均响应 22.41 天
  [openeuler-docker-images] 开启 54，平均响应 1.67 天
  [llvm-project] 开启 40，平均响应 18.32 天
  ...
```

---

### get_prs_detail ❌
**测试问题**：查看 openEuler 社区最近的 PR 详情
**调用参数**：community=openEuler, page_num=1, page_size=3
**返回结果**：`API 错误：（空错误信息）`

---

### get_repo_user_list ❌
**测试问题**：openEuler 社区的活跃用户列表
**调用参数**：community=openEuler, page=1, page_size=5
**返回结果**：`API 错误：系统内部出现错误`

---

## CI

### get_ci_metrics ❌
**测试问题**：openEuler 社区 2026 年 Q1 的 CI 指标
**调用参数**：community=openEuler, start_time=2026-01-01, end_time=2026-03-10
**返回结果**：`API 错误：系统内部出现错误`

---

## 论坛

### get_forum_agg ❌
**测试问题**：openEuler 社区论坛帖子汇总
**调用参数**：community=openEuler, page_num=1, page_size=5
**返回结果**：`API 错误：用户未登录`
**备注**：需要登录态，MCP 调用不携带 session

---

### get_forum_tag_agg ⚠️
**测试问题**：openEuler 社区论坛标签统计
**调用参数**：community=openEuler
**返回结果**：`暂无论坛标签数据`（接口正常但无数据）

---

### get_forum_detail ✅
**测试问题**：openEuler 社区论坛最新帖子列表
**调用参数**：community=openEuler
**返回结果**：
```
论坛帖子详情（共 549 条，55 页）：
  [2026-03-09] issue关联PR — 回复 0，浏览 0
  [2026-03-09] openEuler24.03安装vmwareworkstation启动时 gcc找不到 报错处理 — 回复 0，浏览 0
  [2026-03-07] 服务器全天待命，飞书Agent秒响应：OpenClaw x openEuler 容器化部署指南 — 回复 0，浏览 0
  ...
```

---

## SIG

### get_sig_leverage_ratio ⚠️
**测试问题**：openEuler 社区各 SIG 的撬动比
**调用参数**：community=openEuler
**返回结果**：`SIG 撬动比统计（总外部代码占比：1）`（接口正常，但无明细数据）

---

## 用户

### get_users_page ❌
**测试问题**：openEuler 社区开发者列表
**调用参数**：community=openEuler, page_num=1, page_size=3
**返回结果**：`API 错误：系统内部出现错误`

---

### get_users_trend ❌
**测试问题**：openEuler 社区 2026 年 Q1 开发者趋势（按月）
**调用参数**：community=openEuler, start_date=2026-01-01, end_date=2026-03-10, interval=month
**返回结果**：`API 错误：系统内部出现错误`

---

## 服务平台

### get_source_total ❌
**测试问题**：openEuler 社区服务平台汇总数据
**调用参数**：community=openEuler
**返回结果**：`API 错误：系统内部出现错误`

---

### get_source_trend ❌
**测试问题**：openEuler 社区服务平台趋势（按月）
**调用参数**：community=openEuler, interval=month
**返回结果**：`API 错误：系统内部出现错误`

---

## 注册用户

### get_regist_user_detail ❌
**测试问题**：openEuler 社区注册用户详情
**调用参数**：community=openEuler, page_num=1, page_size=3
**返回结果**：`API 错误：系统内部出现错误`

---

## 组织/企业

### get_company_detail ❌
**测试问题**：openEuler 社区参与企业详情
**调用参数**：community=openEuler, page_num=1, page_size=3
**返回结果**：`API 错误：系统内部出现错误`

---

### get_company_trend ❌
**测试问题**：openEuler 社区企业参与趋势（按月）
**调用参数**：community=openEuler, interval=month
**返回结果**：`API 错误：系统内部出现错误`

---

## 贡献

### get_contributes_topn ✅
**测试问题**：openEuler 社区按公司类型的 PR 贡献 Top5 排名
**调用参数**：community=openEuler, event=pr, metric=company_type, topn=5
**返回结果**：
```
贡献 Top5（维度：company_type，类型：pr）：
  1. 企业 — 23705
  2. 华为 — 13573
  3. 个人贡献者 — 12616
  4. robot — 3913
  5. 学生 — 13
```

---

### get_contributes_topn_item ❌
**测试问题**：openEuler 社区 kernel 仓库的 PR 贡献趋势
**调用参数**：community=openEuler, event=pr, metric=repo, metric_val=kernel, interval=month
**返回结果**：`API 错误：body[metricVal]数据类型错误`
**备注**：metricVal 参数类型可能需要调整

---

### get_contributes_page ❌
**测试问题**：openEuler 社区贡献汇总分页列表
**调用参数**：community=openEuler, page_num=1, page_size=3
**返回结果**：`API 错误：系统内部出现错误`

---

### get_contributes_trend ❌
**测试问题**：openEuler 社区 2026 年 Q1 PR 贡献趋势（按月）
**调用参数**：community=openEuler, start_date=2026-01-01, end_date=2026-03-10, event_list=pr, interval=month
**返回结果**：`API 错误：系统内部出现错误`

---

## 其他

### get_metric_dict ✅
**测试问题**：获取所有可用指标的字典
**调用参数**：无
**返回结果**：返回约 120+ 个指标定义，含名称、中文名、单位、适用范围等

---

### get_filter_options ✅
**测试问题**：openEuler 社区 Issue 页面的筛选条件有哪些？
**调用参数**：community=openEuler, tab=issue
**返回结果**：返回 15 个筛选条件组合（source/namespace/internal/private 维度）

---

### get_account_trend ❌
**测试问题**：openEuler 社区账号注册趋势
**调用参数**：community=openEuler
**返回结果**：`API 错误：系统内部出现错误`

---

## 测试汇总

| 状态 | 数量 | 接口列表 |
|------|------|---------|
| ✅ 通过 | 12 | get_community_health, list_communities, get_community_list, get_issues_aggregate, get_issues_agg_page, get_issues_detail, get_issue_ref_pr, get_prs_aggregate, get_prs_agg_page, get_forum_detail, get_contributes_topn, get_metric_dict, get_filter_options |
| ⚠️ 部分 | 2 | get_forum_tag_agg（无数据）, get_sig_leverage_ratio（无明细）|
| ❌ 失败 | 24 | 其余接口 |

### 失败分类

- **用户未登录**：get_forum_agg
- **参数类型错误**：get_contributes_topn_item（metricVal 参数）
- **系统内部错误**：其余 22 个接口

### 问题分析

1. **大量接口返回"系统内部出现错误"**：可能是这些接口需要特定的请求参数或权限，建议排查 `server_apis.py`、`query_apis.py` 中对应接口的参数传递方式。

2. **CLA 接口 404**：`get_cla_user_list` 和 `get_cla_trend` 接口路径可能已变更，需要更新。

3. **get_contributes_topn_item 参数错误**：`metric_val` 参数需要传递特定格式，建议查看 API 文档确认正确格式。

4. **get_forum_agg 需要登录**：论坛聚合接口需要认证，MCP 服务可能需要配置认证信息。
