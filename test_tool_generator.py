#!/usr/bin/env python3
"""测试 tool_generator.py 中的 tool 注册是否成功."""

import asyncio

from lib.tool_generator import _build_docstring, _build_signature, _make_tool_function, generate_all_tools
from lib.template_loader import load_all_templates
from mcp.server.fastmcp import FastMCP


def test_templates_loaded():
    """测试模板加载是否成功."""
    templates = load_all_templates()
    print(f"✓ 加载了 {len(templates)} 个模板")
    for t in templates:
        print(f"  - {t.name}: {t.description[:60]}...")
    assert len(templates) > 0, "模板加载失败"
    return templates


def test_tool_function_generation():
    """测试工具函数生成是否成功."""
    templates = load_all_templates()
    for template in templates:
        tool_fn = _make_tool_function(template)
        assert tool_fn.__name__ == template.name, f"工具名称不匹配：{tool_fn.__name__}"
        assert tool_fn.__doc__, f"工具 {template.name} 缺少 docstring"
        assert tool_fn.__signature__, f"工具 {template.name} 缺少 signature"
        print(f"✓ 工具 {template.name} 生成成功")


def test_mcp_registration():
    """测试工具是否成功注册到 MCP."""
    mcp = FastMCP("test-om-metrics")
    templates = load_all_templates()
    
    before_count = len(mcp._tool_manager._tools) if hasattr(mcp._tool_manager, '_tools') else 0
    print(f"注册前工具数：{before_count}")
    
    generate_all_tools(mcp, templates)
    
    after_count = len(mcp._tool_manager._tools) if hasattr(mcp._tool_manager, '_tools') else 0
    print(f"注册后工具数：{after_count}")
    
    assert after_count == before_count + len(templates), (
        f"工具注册失败：期望 {before_count + len(templates)} 个，实际 {after_count} 个"
    )
    
    print("\n已注册的工具列表:")
    for name, tool in mcp._tool_manager._tools.items():
        print(f"  - {name}")
    
    print(f"\n✓ 成功注册 {len(templates)} 个工具到 MCP")
    return mcp


async def test_tool_execution():
    """测试工具函数能否正常执行."""
    templates = load_all_templates()
    if not templates:
        return
    
    template = templates[0]
    tool_fn = _make_tool_function(template)
    
    print(f"\n测试执行工具：{template.name}")
    try:
        result = await tool_fn()
        print(f"执行结果：{result[:100]}...")
        print(f"✓ 工具 {template.name} 执行成功")
    except Exception as e:
        print(f"✗ 工具 {template.name} 执行失败：{e}")


def test_param_signature():
    """测试参数签名生成是否正确."""
    
    templates = load_all_templates()
    for template in templates:
        sig = _build_signature(template)
        print(f"✓ 工具 {template.name} 签名：{sig}")


def test_docstring_generation():
    """测试 docstring 生成是否正确."""
    
    templates = load_all_templates()
    for template in templates:
        docstring = _build_docstring(template)
        print(f"✓ 工具 {template.name} docstring 第一行：{docstring.split(chr(10))[0]}")


if __name__ == "__main__":
    print("=" * 70)
    print("codegen.py tool 注册测试")
    print("=" * 70)
    
    print("\n[1/6] 测试模板加载...")
    templates = test_templates_loaded()
    
    print("\n[2/6] 测试参数签名生成...")
    test_param_signature()
    
    print("\n[3/6] 测试 docstring 生成...")
    test_docstring_generation()
    
    print("\n[4/6] 测试工具函数生成...")
    test_tool_function_generation()
    
    print("\n[5/6] 测试 MCP 注册...")
    test_mcp_registration()
    
    print("\n[6/6] 测试工具执行...")
    asyncio.run(test_tool_execution())
    
    print("\n" + "=" * 70)
    print("所有测试通过！")
    print("=" * 70)
