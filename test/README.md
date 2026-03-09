# 测试说明

## 运行测试

```bash
cd test
python test_mcp.py
```

## 测试内容

`test_mcp.py` 模拟真实 PPT 制作场景，构造问题并调用各 MCP 工具验证返回结果。

测试覆盖以下功能：
- 社区列表查询
- 指标字典获取
- 热点仓库查询
- 活跃仓库统计
- 企业和个人贡献排行
- Issue/PR 聚合统计
- 按 SIG 分组统计
- 活跃用户列表
- CLA 签署统计和趋势
- CI 指标查询

## 故障排查

### 测试失败

1. 确认网络连接正常，可访问远程 API：`curl https://datastat.osinfra.cn/server/`
2. 检查社区名称是否正确（使用 `list_communities` 工具查看支持的社区）
3. 查看具体错误信息，确认 API 返回状态
