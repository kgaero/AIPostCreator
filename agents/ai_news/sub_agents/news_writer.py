"""Agent that writes the final AI news dispatch."""

from google.adk.agents import LlmAgent

from .. import prompt

MODEL = "gemini-2.5-pro"


news_writer_agent = LlmAgent(
  name="news_writer_agent",
  model=MODEL,
  description=(
    "Synthesizes verified research into a concise AI news post with inline "
    "citations and explicit word counts."
  ),
  instruction=prompt.NEWS_WRITER_PROMPT,
  output_key="ai_news_post",
)
"""Writing agent that guarantees brevity and sourcing discipline."""
