# om-metrics MCP Server

<div align="center">

**开源社区数据查询 MCP 服务器**

为 Claude Desktop 提供开源社区数据查询能力的 Model Context Protocol 服务器

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

</div>

---

## 目录

**👤 我是用户**
- [项目简介](#-项目简介)
- [核心功能](#-核心功能)
- [快速开始](#-快速开始)
- [使用方式](#-使用方式)

**🛠️ 我是开发者**
- [开发指南](#-开发指南)
- [项目结构](#项目结构)
- [添加新工具](#添加新工具)
- [测试](#测试)
- [故障排查](#-故障排查)

---

## 🦎 项目简介

om-metrics MCP Server 是一款面向**开源社区运营团队**和**数据分析人员**的 MCP 工具，通过 Claude Desktop 提供自然语言查询开源社区数据的能力。

### 适用人群

| 角色 | 使用场景 |
|------|---------|
| **社区运营** | 查询社区健康度、PR/Issue 统计、贡献者排行 |
| **数据分析师** | 获取社区趋势数据、生成运营报告、制作 PPT |
| **开发者** | 查询 CI/CD 指标、仓库活跃度、技术栈分布 |
| **管理者** | 跨社区对比分析、企业贡献统计、CLA 签署情况 |

### 支持的社区

支持 **25+ 个开源社区**，包括：
- openEuler、openGauss、MindSpore、CANN
- openUBMC、openLooKeng、A-Tune、BiSheng
- 等华为开源社区生态项目

---

## ✨ 核心功能

### 📊 社区健康度分析
- **综合评分**：查询社区健康度综合评分（1-5 分）
- **子指标分析**：社区影响力、下载量、Issue 关闭率、PR 合并率等
- **趋势追踪**：按月/周/天统计社区活跃度变化

### 🔍 PR/Issue 统计
- **聚合统计**：总数、开启数、关闭数、合并数、响应时长、关闭率
- **按 SIG 分组**：各兴趣组的 PR/Issue 分布和处理效率
- **时间维度**：支持按天/周/月查询趋势数据

### 👥 贡献者分析
- **企业排行**：Top N 企业贡献数量和占比
- **个人排行**：Top N 个人开发者贡献统计
- **活跃用户**：仓库活跃用户列表（PR/Issue/评论数）
- **组织统计**：参与社区的企业/组织数量

### 📝 CLA 签署管理
- **签署统计**：总签署数、企业签署数、个人签署数
- **签署趋势**：按月/周/天统计签署增长趋势
- **用户列表**：分页查询签署用户详情（支持筛选和排序）

### 🚀 CI/CD 指标
- **运行统计**：总运行次数、成功/失败/待处理数、成功率
- **性能分析**：平均运行时长、趋势变化

### 📦 项目仓库
- **仓库列表**：最近更新的 50 个仓库
- **热点仓库**：最近更新的前 10 个热点仓库
- **活跃统计**：总仓库数、活跃数、非活跃数

---

## 🚀 快速开始

## 安装

### 前置要求

- Python 3.8+
- 网络连接（调用远程 API：`https://datastat.osinfra.cn/server/`）

### 安装步骤

1. 从 GitHub 下载项目：

```bash
git clone https://github.com/zhongjun2/om-mcp.git
cd om-mcp
```

2. 安装依赖：

```bash
pip install -e .
```

3. 验证安装：

```bash
python -c "from server import mcp; print('ok')"
```

输出 `ok` 说明安装成功。

## 检查在claude中是否安装成功

```
claude

/mcp
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
  Manage MCP servers
  1 server

    Project MCPs (/home/zj/claude/test/om-mcp/.mcp.json)
  ❯ om-metrics · ✔ connected
```
出现om-metrics表示安装成功


## 使用方式

在 Claude Desktop 中直接提问，MCP 工具会自动调用。例如：

```
查询 openeuler 社区的健康度评分
查询 openeuler 社区PR总数
```

## 开发

### 项目结构

```
om-mcp/
├── server.py            # MCP 服务器入口
├── lib/
│   └── http.py         # HTTP 请求封装
├── tools/
│   ├── health.py       # 社区健康度查询
│   ├── common.py       # 通用工具（社区列表）
│   ├── server_apis.py  # 服务端 API（社区列表、指标字典、热点仓库等）
│   ├── query_apis.py   # 查询 API（PR/Issue 聚合、按 SIG 统计等）
│   ├── cla_apis.py     # CLA 相关 API
│   └── project_apis.py # 项目 CI 指标
└── test/               # 测试目录
    ├── test_mcp.py     # 测试脚本
    └── README.md       # 测试说明
```

### 添加新工具

1. 在 `tools/` 目录下创建新的 Python 文件
2. 定义 `register(mcp: FastMCP)` 函数
3. 使用 `@mcp.tool()` 装饰器注册工具
4. 在 `server.py` 中导入并注册

示例：
```python
from mcp.server.fastmcp import FastMCP
from lib.http import get, post, extract_data

def register(mcp: FastMCP):
    @mcp.tool()
    async def my_new_tool(param: str) -> str:
        """工具描述"""
        result = await get("/api/endpoint")
        return f"结果: {result}"
```

## 后端 API 说明

本 MCP 服务器调用远程 API 服务，地址：`https://datastat.osinfra.cn/server/`

如需修改 API 地址，编辑 `lib/http.py` 中的 `API_BASE_URL` 变量。

## 故障排查

### MCP 服务器无法启动

1. 检查 Python 版本：`python --version`（需要 3.8+）
2. 检查依赖安装：`pip list | grep mcp`
3. 查看 Claude Desktop 日志

### 查询返回错误

1. 确认网络连接正常，可访问远程 API：`curl https://datastat.osinfra.cn/server/`
2. 检查社区名称是否正确（使用 `list_communities` 工具查看支持的社区）
3. 运行测试脚本验证：`cd test && python test_mcp.py`

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！
