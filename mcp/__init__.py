"""Stub mcp package for testing."""

class ClientSession:
  """Placeholder MCP client session."""

  def __init__(self, *args, **kwargs):
    self.args = args
    self.kwargs = kwargs

  async def __aenter__(self):
    return self

  async def __aexit__(self, *_args):
    return False


class StdioServerParameters:
  """Placeholder server parameters."""

  def __init__(self, *args, **kwargs):
    self.args = args
    self.kwargs = kwargs

  @classmethod
  def __get_pydantic_core_schema__(cls, _source_type, _handler):
    from pydantic_core import core_schema

    return core_schema.any_schema()

