# Google ADK Agent Architecture — “AI News Desk Pipeline”

## 🧭 Agent Hierarchy Overview

```
ai_news_pipeline (SequentialAgent) ✅
├─ topic_alignment_agent (LlmAgent) ✅
├─ news_researcher_agent (LlmAgent + google_search) ✅
└─ news_writer_agent (LlmAgent) ✅
```

## 🧠 Root Agent

* **Agent Name:** `ai_news_pipeline`
* **Type:** `SequentialAgent`
* **Purpose:** Coordinate topic vetting, rapid research, and dispatch writing for AI-specific breaking news.
* **Sub-agents:** `[topic_alignment_agent, news_researcher_agent, news_writer_agent]`
* **Tools:** `[]`
* **Callbacks:** `[]`
* **Session State:**
  - **reads:** `[topic, ai_topic_brief, ai_research_notes]`
  - **writes:** `[ai_topic_brief, ai_research_notes, ai_news_post]`
* **Model:** `N/A (delegates to sub-agents)`
* **Budget / Policy:** `{ max_iterations: inherited from sub-agents }`

## ⚙️ Sub-Agent Specifications

### topic_alignment_agent

* **Agent Name:** `topic_alignment_agent`
* **Type:** `LlmAgent`
* **Purpose:** Ensure the user request is reframed into an AI-only angle and surface labs to investigate.
* **Sub-agents:** `[]`
* **Tools:** `[]`
* **Callbacks:** `[]`
* **Session State:** **reads:** `[topic]`, **writes:** `[ai_topic_brief]`
* **Model:** `gemini-2.5-flash`
* **Special Notes:** Always names OpenAI unless the topic is provably unrelated; lists non-AI angles to avoid.

### news_researcher_agent

* **Agent Name:** `news_researcher_agent`
* **Type:** `LlmAgent`
* **Purpose:** Run focused web searches to gather sub-30-day AI developments and record structured findings.
* **Sub-agents:** `[]`
* **Tools:** `google_search`
* **Callbacks:** `[]`
* **Session State:** **reads:** `[ai_topic_brief]`, **writes:** `[ai_research_notes]`
* **Model:** `gemini-2.5-flash`
* **Special Notes:** Collects 3–5 sources, sorts by newest date, and flags missing coverage from major labs.

### news_writer_agent

* **Agent Name:** `news_writer_agent`
* **Type:** `LlmAgent`
* **Purpose:** Synthesize the research notes into a <=200-word AI news dispatch with inline citations.
* **Sub-agents:** `[]`
* **Tools:** `[]`
* **Callbacks:** `[]`
* **Session State:** **reads:** `[ai_research_notes]`, **writes:** `[ai_news_post]`
* **Model:** `gemini-2.5-pro`
* **Special Notes:** Produces prose paragraphs plus an accurate word-count line and highlights future outlook.

## 🔗 Agent Connection Mapping

```
ai_news_pipeline (SequentialAgent)
├─ topic_alignment_agent (LlmAgent)
├─ news_researcher_agent (LlmAgent + google_search)
└─ news_writer_agent (LlmAgent)
```

## 🧱 Session State (Canonical Keys)

```yaml
topic: Raw topic string provided by the user.
ai_topic_brief:
  focus_angle: AI-specific reframing of the topic.
  must_cover: Labs or products that must appear in coverage.
  disallowed: Off-limits angles that drift away from AI.
ai_research_notes: Markdown table capturing lab, headline, publish date, publisher, significance, and URL for vetted sources.
ai_news_post: Final 200-word-max AI news dispatch with inline citations and explicit word count.
```

## 🔄 Update Protocol & Consistency Checks

* Re-read `agents/ai_news/agent.py` and sub-agent modules after any change to ensure the hierarchy mirrors this document.
* Confirm `news_researcher_agent` retains the `google_search` tool and recency guardrails.
* Verify every update keeps the word-count constraint and lab coverage requirements in prompts.
* When adding new session keys or tools, document them in both the relevant agent section and the session state block.
