"""Agent that reframes user topics into AI-specific briefs."""

from google.adk.agents import LlmAgent

from .. import prompt

MODEL = "gemini-2.5-flash"


topic_alignment_agent = LlmAgent(
  name="topic_alignment_agent",
  model=MODEL,
  description=(
    "Ensures the requested topic is scoped to artificial intelligence and "
    "identifies priority labs to investigate."
  ),
  instruction=prompt.TOPIC_ALIGNMENT_PROMPT,
  output_key="ai_topic_brief",
)
"""Assignment editor that keeps coverage anchored in AI developments."""
