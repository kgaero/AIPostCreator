"""Minimal google namespace package for tests."""

from pathlib import Path

_pkg_dir = Path(__file__).resolve().parent
_refs_google = _pkg_dir.parent / "refs" / "adk-python" / "src" / "google"

__path__ = [str(_pkg_dir)]
if _refs_google.exists():
  __path__.append(str(_refs_google))
