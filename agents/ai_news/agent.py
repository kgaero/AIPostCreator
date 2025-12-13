"""Root AI News agent wiring."""

from google.adk import agents

from . import prompt
from .sub_agents import news_researcher_agent
from .sub_agents import news_writer_agent
from .sub_agents import topic_alignment_agent


ai_news_pipeline = agents.SequentialAgent(
  name="ai_news_pipeline",
  description=(
    "Coordinates topic alignment, rapid research, and news writing to produce "
    "a concise AI news dispatch."
  ),
  sub_agents=[
    topic_alignment_agent,
    news_researcher_agent,
    news_writer_agent,
  ],
)
"""Sequential pipeline that runs the AI newsroom workflow."""

# The pipeline is the runnable root agent entry point.
root_agent = ai_news_pipeline

# Provide a helpful summary for documentation consumers.
ROOT_AGENT_SUMMARY = prompt.SYSTEM_PROMPT
