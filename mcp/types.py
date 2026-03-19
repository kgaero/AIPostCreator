"""Stub types for mcp package."""

class ListToolsResult:
  """Placeholder MCP list result."""

  def __init__(self, *args, **kwargs):
    self.tools = []


class Tool:
  """Placeholder MCP tool."""

  def __init__(self, *args, **kwargs):
    self.name = kwargs.get("name", "stub_tool")
