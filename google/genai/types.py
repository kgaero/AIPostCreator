"""Minimal type stubs to satisfy google.adk imports during tests."""

from dataclasses import dataclass
from typing import Any

from pydantic_core import core_schema


@dataclass
class GenerateContentConfig:
  """Simplified stand-in for the Google GenAI configuration object."""

  temperature: float | None = None
  tools: list[Any] | None = None


@dataclass
class Tool:
  """Minimal placeholder for the GenAI tool descriptor."""

  google_search: Any | None = None
  google_search_retrieval: Any | None = None


class Type:
  """Simplified enum for GenAI schema types."""

  STRING = "string"
  NUMBER = "number"
  INTEGER = "integer"
  BOOLEAN = "boolean"
  ARRAY = "array"
  OBJECT = "object"
  NULL = "null"
  TYPE_UNSPECIFIED = "unspecified"


@dataclass
class GoogleSearch:
  """Placeholder Google Search tool descriptor."""

  pass


@dataclass
class GoogleSearchRetrieval:
  """Placeholder Google Search retrieval descriptor."""

  pass


def __getattr__(name: str) -> type[Any]:
  """Dynamically create placeholder classes for unused GenAI types."""

  def _constructor(self, *args: Any, **kwargs: Any) -> None:
    self.args = args
    self.kwargs = kwargs

  def _schema(cls, _source_type: Any, _handler: Any) -> Any:
    return core_schema.any_schema()

  placeholder = type(
    name,
    (),
    {
      "__init__": _constructor,
      "__get_pydantic_core_schema__": classmethod(_schema),
    },
  )
  globals()[name] = placeholder
  return placeholder
