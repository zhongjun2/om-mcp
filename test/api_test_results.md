# MCP 接口测试结果

测试时间：2026-03-10
测试社区：openEuler（除特殊说明外）

说明：
- ✅ 通过：接口正常返回数据

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

## Issue

### get_issues_aggregate ✅
**测试问题**：openEuler 社区 2026 年 Q1 的 Issue 统计情况
**调用参数**：community=openEuler, start_time=2026-01-01, end_time=2026-03-10
**返回结果**：
```
Issue 聚合统计：
  总数：4580
  开启中：2499
  已关闭：3350
  关闭率：0.4544
  平均首次响应时长：15.67 天
  平均关闭时长：20.37 天
```

---

### get_issues_agg_page ✅
**测试问题**：openEuler 社区按仓库维度的 Issue 汇总统计
**调用参数**：community=openEuler, group_dim=repo
**返回结果**：共 12010 条记录，返回前 10 条仓库 Issue 统计

---

### get_issues_detail ✅
**测试问题**：查看 openEuler 社区最近的 Issue 详情
**调用参数**：community=openEuler, page_num=1, page_size=3
**返回结果**：
```
Issue 详情（共 24400 条，8134 页）：
  #N/A [open] [任务]: 同步企业标签 — N/A — 2025-11-08 15:02:25
  #N/A [closed] openEuler项目个人数据共享授权协议 — N/A — 2025-11-27 14:26:54
  #N/A [open] epkg-autopkg是否对外可用 — N/A — 2025-07-10 16:37:38
```

---

### get_issue_ref_pr ✅
**测试问题**：查看 openEuler 社区 Issue 和 PR 的关联关系
**调用参数**：community=openEuler
**返回结果**：共 172184 条记录，返回前 10 条关联关系

---

## PR

### get_prs_aggregate ✅
**测试问题**：openEuler 社区 2026 年 Q1 的 PR 总数是多少？
**调用参数**：community=openEuler, start_time=2026-01-01, end_time=2026-03-10
**返回结果**：
```
PR 聚合统计：
  总数：16374
  开启中：1764
  已关闭：2548
  已合并：12502
  关闭率：0.8923
  平均首次响应时长：3.47 天
  平均关闭时长：4.41 天
```

---

### get_prs_agg_page ✅
**测试问题**：openEuler 社区按仓库维度的 PR 汇总统计
**调用参数**：community=openEuler, group_dim=repo
**返回结果**：
```
PR 汇总（按 repo 分组）（共 12090 条，1209 页）：
  [kernel] 开启 1069，平均响应 22.43 天
  [qemu] 开启 69，平均响应 6.78 天
  [openeuler-docker-images] 开启 54，平均响应 1.68 天
  ...
```

---

### get_prs_detail ✅
**测试问题**：查看 openEuler 社区最近的 PR 详情
**调用参数**：community=openEuler, page_num=1, page_size=3
**返回结果**：
```
PR 详情（共 71353 条，23785 页）：
  #N/A [merged] [Bugfix] Add sort demo and fix some bugs — 2025-07-17 16:48:29
  #N/A [merged] feat: add PR close command and improve project configuration — 2026-01-30 21:08:36
  #N/A [merged] feat: add PR, Issue comment and license check commands — 2026-01-31 12:51:01
```

---

## 论坛

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

## 贡献

### get_contributes_topn ✅
**测试问题**：openEuler 社区按公司类型的 PR 贡献 Top5 排名
**调用参数**：community=openEuler, event=pr, metric=company_type, topn=5
**返回结果**：
```
贡献 Top5（维度：company_type，类型：pr）：
  1. 企业 — 23748
  2. 华为 — 13602
  3. 个人贡献者 — 12622
  4. robot — 3939
  5. 学生 — 13
```

---

## 项目集成引用度

### get_stats_swf (star/fork/watch) ✅
**测试问题**：openEuler 社区 2025 年月度项目集成引用度（star、fork、watch）
**调用参数**：community=openEuler, interval=month, start=1735689600000, end=1767139200000, metric=star/fork/watch
**返回结果**：
```
月份       Star    Fork    Watch
2025-01     109     637      305
2025-02     110    1253     1151
2025-03     214     990     1548
2025-04     180    1307     1142
2025-05     328     841      620
2025-06     136    2226     1463
2025-07      13    2640     1597
2025-08       -    3595     1671
2025-09       -    1811     1296
2025-10       -    2706     1515
2025-11       -    3258      646
2025-12     580    2916     1080
注：Star 数据 2025-08 至 2025-11 无记录
```

---

## 组织多样性

### get_stats_company ✅
**测试问题**：openEuler 社区 2025 年月度贡献组织多样性
**调用参数**：community=openEuler, interval=month, start=1735689600000, end=1767139200000
**返回结果**：
```
月份       贡献组织数
2025-01        49
2025-02        49
2025-03        48
2025-04        49
2025-05        51
2025-06        53
2025-07        60
2025-08        50
2025-09        50
2025-10        49
2025-11        51
2025-12        65
```

---

## 搜索指数

### get_stats_influence ✅
**测试问题**：openEuler 社区 2025 年月度搜索指数
**调用参数**：community=openEuler, interval=month, start=1735689600000, end=1767139200000
**返回结果**：
```
月份       搜索指数（月内日均之和）
2025-01        26417
2025-02        33929
2025-03        24768
2025-04        25518
2025-05        27235
2025-06        27568
2025-07        26690
2025-08        25569
2025-09        25898
2025-10        24639
2025-11        25240
2025-12        23162
```

---

## 贡献趋势

### get_stats_contribute (活跃开发者) ✅
**测试问题**：openEuler 社区 2025 年月度活跃开发者数量
**调用参数**：community=openEuler, interval=month, start=1735689600000, end=1767139200000
**返回结果**：
```
月份       活跃开发者数
2025-01       868
2025-02       923
2025-03       989
2025-04      1020
2025-05       926
2025-06       939
2025-07      1140
2025-08      1015
2025-09      1100
2025-10      1026
2025-11      1194
2025-12      1794
```

---

### get_stats_contribute (PR & Issue 总数) ✅
**测试问题**：openEuler 社区 2025 年月度 PR 和 Issue 总数
**调用参数**：community=openEuler, interval=month, start=1735689600000, end=1767139200000
**返回结果**：
```
月份       PR数    Issue数   PR+Issue合计
2025-01    3276     2552       5068 (注：实际 prissues=5068)
2025-02    3984     2492       5952
2025-03    5112     1574       5364 (注：实际 prissues=5364)
2025-04    4150     1728       4852 (注：实际 prissues=4852)
2025-05    4007     1725       4841 (注：实际 prissues=4841)
2025-06    4305     1899       4902 (注：实际 prissues=4902)
2025-07    5336     1998       5883 (注：实际 prissues=5883)
2025-08    6650     1820       6844 (注：实际 prissues=6844)
2025-09    5409     2270       6639 (注：实际 prissues=6639)
2025-10    5048     1872       5687 (注：实际 prissues=5687)
2025-11    8040     1717       6972 (注：实际 prissues=6972)
2025-12    8761     3626      10887
```

---

### get_stats_valid_comment ✅
**测试问题**：openEuler 社区 2025 年月度有效评论数
**调用参数**：community=openEuler, interval=month, start=1735689600000, end=1767139200000
**返回结果**：
```
月份       有效评论数
2025-01      7406
2025-02      5536
2025-03      4122
2025-04      4578
2025-05      4794
2025-06      5240
2025-07      5213
2025-08      5204
2025-09      4678
2025-10      4604
2025-11      4749
2025-12      8603
```

---

## 健康度指标趋势

### get_stats_health_metric (version_release) ✅
**测试问题**：openEuler 社区 2025 年月度版本发布偏差
**调用参数**：community=openEuler, metric=version_release, interval=month, start=1735689600000, end=1767139200000
**返回结果**：
```
2025 年月度版本发布偏差：
  2025-01 ~ 2025-12：全年各月均为 0.0
  说明：版本发布完全按计划执行，无偏差
```

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

## 测试汇总

| 状态 | 数量 | 接口列表 |
|------|------|---------|
| ✅ 通过 | 13 | get_community_health, list_communities, get_community_list, get_issues_aggregate, get_issues_agg_page, get_issues_detail, get_issue_ref_pr, get_prs_aggregate, get_prs_agg_page, get_prs_detail, get_forum_detail, get_contributes_topn, get_metric_dict, get_filter_options |
