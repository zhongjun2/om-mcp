# OM-MCP 项目开发规范

## 项目概述

本项目是基于 FastMCP 框架的 MCP (Model Context Protocol) 服务，用于查询开源社区的各类指标数据。

## 技术栈

- **语言**: Python 3.x
- **框架**: FastMCP (`mcp.server.fastmcp`)
- **HTTP 客户端**: httpx (异步)
- **Base URL**: `https://datastat.osinfra.cn/server`

## 项目结构

```
om-mcp/
├── server.py              # 入口文件，注册所有工具模块
├── lib/
│   └── http.py           # HTTP 请求封装
├── tools/
│   ├── health.py         # 社区健康度
│   ├── common.py         # 通用工具
│   ├── server_apis.py    # 服务端 API
│   ├── query_apis.py     # 查询 API
│   ├── cla_apis.py       # CLA 相关 API
│   ├── project_apis.py   # 项目 API
│   └── general_apis.py   # 通用查询 API
├── test/                 # 测试用例目录
├── API_LIST.md          # 接口列表文档
└── CLAUDE.md            # 本文件
```

## 开发规范

### 1. 添加新的 MCP 工具方法

当需要添加新的 MCP 工具方法时，必须遵循以下步骤：

#### 步骤 1: 实现工具函数

在 `tools/` 目录下的相应模块中添加工具函数：

```python
@mcp.tool()
async def your_new_tool(param1: str = "", param2: str = "") -> str:
    """
    工具描述（中文）。

    Args:
        param1: 参数1说明
        param2: 参数2说明
    """
    # 实现逻辑
    pass
```

#### 步骤 2: 注册模块

如果是新模块，在 `server.py` 中注册：

```python
import tools.your_module as your_module

your_module.register(mcp)
```

#### 步骤 3: 更新接口文档

在 `API_LIST.md` 中添加新接口的文档说明，包括：
- 接口名称
- 功能描述
- 参数列表（类型、是否可选、默认值）
- 返回值说明

#### 步骤 4: 编写测试用例

**必须为新接口编写测试用例**，在 `test/` 目录下创建或更新测试文件：

```python
# test/test_your_module.py
# 测试问题: 描述测试场景
# 预期结果: 描述预期返回的数据
```

#### 步骤 5: 执行测试并记录结果

运行测试并将测试问题、返回结果记录到 `test/` 目录下的相应文件中。

### 2. 测试规范

#### 测试文件命名

- 按功能模块组织：`test_<module_name>.md`
- 例如：`test_issues.md`, `test_prs.md`, `test_cla.md`

#### 测试内容格式

每个测试用例应包含：

```markdown
## 接口名称: get_xxx

### 测试用例 1
**测试问题**: 查询 openEuler 社区的 XXX 数据
**调用参数**:
- community: openEuler
- start_time: 2026-01-01
- end_time: 2026-03-10

**返回结果**:
```
<实际返回的数据>
```

**测试状态**: ✅ 通过 / ❌ 失败
**测试时间**: 2026-03-10
```

### 3. 代码规范

#### HTTP 请求

使用 `lib/http.py` 中封装的方法：

```python
from lib.http import get, post, extract_data

# GET 请求
data = await get("/api/path", {"param": "value"})

# POST 请求
data = await post("/api/path", {"param": "value"})

# 提取数据（自动处理双层嵌套）
result = extract_data(data)
```

#### 时间参数处理

- 对外接口使用 `YYYY-MM-DD` 格式
- 内部 API 如需毫秒时间戳，使用 `_date_to_ms()` 转换

```python
from lib.http import _date_to_ms

timestamp = _date_to_ms("2026-03-10")  # 转为毫秒时间戳
```

#### 社区名称处理

社区名称大小写不敏感，统一转为小写处理：

```python
community = community.lower()
```

### 4. 文档维护

#### API_LIST.md

- 每次添加新接口必须更新此文档
- 按功能分类组织
- 包含完整的参数说明和返回值描述
- 更新"更新记录"部分

#### CLAUDE.md (本文件)

- 记录项目架构变更
- 更新开发规范
- 记录重要的技术决策

### 5. Git 提交规范

提交信息格式：

```
<type>: <subject>

<body>
```

类型 (type):
- `feat`: 新功能
- `fix`: 修复 bug
- `docs`: 文档更新
- `test`: 测试相关
- `refactor`: 重构
- `style`: 代码格式调整

示例：
```
feat: 添加 get_xxx 接口

- 实现 get_xxx 工具函数
- 更新 API_LIST.md
- 添加测试用例到 test/test_xxx.md
```

## 常见问题

### Q: 如何调试 MCP 工具？

A: 可以使用 MCP Inspector 或直接在代码中添加日志：

```python
import logging
logging.info(f"Debug info: {data}")
```

### Q: API 返回数据格式不一致怎么办？

A: 使用 `extract_data()` 函数，它会自动处理单层和双层嵌套的 data 结构。

### Q: 如何处理可选参数？

A: 使用默认值 `""` 或 `0`，在函数内部判断是否传入：

```python
async def tool(param: str = "") -> str:
    if param:
        # 使用 param
    else:
        # 不使用 param
```

## 参考资料

- [FastMCP 文档](https://github.com/jlowin/fastmcp)
- [MCP 协议规范](https://modelcontextprotocol.io/)
- [项目 API 文档](./API_LIST.md)
- [通用查询 API 说明](./通用查询/CLAUDE.md)
