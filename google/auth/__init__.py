"""Stub google.auth package for testing."""

class Credentials:
  """Placeholder credentials object."""

  def __init__(self, *args, **kwargs):
    self.args = args
    self.kwargs = kwargs


def default(scopes=None, quota_project_id=None):
  return Credentials(), None
