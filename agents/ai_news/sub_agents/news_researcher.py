"""Agent that gathers up-to-date AI news sources."""

from google.adk.agents import LlmAgent
from google.adk.tools import google_search

from .. import prompt

MODEL = "gemini-2.5-flash"


news_researcher_agent = LlmAgent(
  name="news_researcher_agent",
  model=MODEL,
  description=(
    "Uses focused web searches to collect sub-30-day AI announcements and "
    "organize them into structured research notes."
  ),
  instruction=prompt.NEWS_RESEARCHER_PROMPT,
  tools=[google_search],
  output_key="ai_research_notes",
)
"""Research agent that enforces recency and lab coverage requirements."""
