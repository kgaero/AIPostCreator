"""Unit tests for the AI News agent wiring and prompts."""

import sys
from pathlib import Path
import types

repo_root = Path(__file__).resolve().parents[1]
sys.path.append(str(repo_root))
sys.path.append(str(repo_root / "refs" / "adk-python" / "src"))

authlib_stub = types.ModuleType("authlib")
authlib_integrations = types.ModuleType("authlib.integrations")
authlib_requests_client = types.ModuleType("authlib.integrations.requests_client")
authlib_oauth2 = types.ModuleType("authlib.oauth2")
authlib_oauth2_rfc6749 = types.ModuleType("authlib.oauth2.rfc6749")
vertexai_stub = types.ModuleType("vertexai")


class OAuth2Session:
  """Test stub for Authlib's OAuth2Session."""

  def __init__(self, *args, **kwargs):
    self.args = args
    self.kwargs = kwargs


authlib_requests_client.OAuth2Session = OAuth2Session
authlib_integrations.requests_client = authlib_requests_client
authlib_stub.integrations = authlib_integrations
authlib_stub.oauth2 = authlib_oauth2
authlib_oauth2.rfc6749 = authlib_oauth2_rfc6749


class OAuth2Token:
  """Test stub for Authlib's OAuth2Token."""

  def __init__(self, *args, **kwargs):
    self.args = args
    self.kwargs = kwargs


authlib_oauth2_rfc6749.OAuth2Token = OAuth2Token

sys.modules.setdefault("authlib", authlib_stub)
sys.modules.setdefault("authlib.integrations", authlib_integrations)
sys.modules.setdefault(
  "authlib.integrations.requests_client", authlib_requests_client
)
sys.modules.setdefault("authlib.oauth2", authlib_oauth2)
sys.modules.setdefault("authlib.oauth2.rfc6749", authlib_oauth2_rfc6749)
sys.modules.setdefault("vertexai", vertexai_stub)

from agents.ai_news import prompt
from agents.ai_news.agent import ROOT_AGENT_SUMMARY
from agents.ai_news.agent import ai_news_pipeline
from agents.ai_news.agent import root_agent
from agents.ai_news.sub_agents import news_researcher_agent
from agents.ai_news.sub_agents import news_writer_agent
from google.adk.agents import LlmAgent
from google.adk.agents import SequentialAgent
from google.adk.tools.google_search_tool import GoogleSearchTool


def test_root_agent_is_sequential_pipeline() -> None:
  """The root agent should expose the sequential pipeline with correct order."""
  assert root_agent is ai_news_pipeline
  assert isinstance(root_agent, SequentialAgent)
  assert [agent.name for agent in root_agent.sub_agents] == [
    "topic_alignment_agent",
    "news_researcher_agent",
    "news_writer_agent",
  ]


def test_researcher_uses_google_search_tool() -> None:
  """Research agent must include the Google Search tool for recency checks."""
  assert isinstance(news_researcher_agent, LlmAgent)
  assert any(isinstance(tool, GoogleSearchTool) for tool in news_researcher_agent.tools)


def test_writer_prompt_limits_word_count() -> None:
  """Writer prompt should enforce 200-word maximum and inline citations."""
  assert "maximum 200 words" in prompt.NEWS_WRITER_PROMPT
  assert "Word count:" in prompt.NEWS_WRITER_PROMPT
  assert "inline markdown citations" in prompt.NEWS_WRITER_PROMPT


def test_system_prompt_reinforces_ai_scope() -> None:
  """Root summary must remind developers to stay inside AI news coverage."""
  assert "AI news" in ROOT_AGENT_SUMMARY
  assert "Ignore unrelated" in ROOT_AGENT_SUMMARY
