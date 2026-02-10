"""Stubbed google.genai package for unit testing."""

from . import types
from .errors import ClientError


class Client:
  """Placeholder GenAI client used for import compatibility."""

  def __init__(self, *args, **kwargs):
    self.args = args
    self.kwargs = kwargs


class _LiveModule:
  """Minimal container mimicking the google.genai.live namespace."""

  def __getattr__(self, name: str):
    def _placeholder(*_args, **_kwargs):
      return None

    return _placeholder


live = _LiveModule()

__all__ = [
  "types",
  "Client",
  "live",
  "ClientError",
]
