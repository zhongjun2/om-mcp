import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
import tools.common as common

from lib.template_loader import load_all_templates
from lib.tool_generator import generate_all_tools
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("om-metrics")

common.register(mcp)
templates = load_all_templates()
generate_all_tools(mcp, templates)

def main():
    """命令行入口函数"""
    mcp.run()

if __name__ == "__main__":
    main()
