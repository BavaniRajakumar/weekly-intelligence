from datetime import datetime

TOPIC = "agentic commerce, retail AI and the impacts to the retail industry"

AGENT_PROMPT = f"""
You are a research analyst. Search for important news about "{TOPIC}" 
from the past 7 days. Provide:

1. Top 3-5 stories. For EACH story you MUST include:
   - A 2-3 sentence summary
   - The publication name
   - A direct URL to the source
   - The publication date
   Format each story like this:
   **[Story Title]**
   Summary: ...
   Source: [Publication Name] — [URL] — [Date]

2. Key emerging themes (2-3 bullets)
3. One surprising or underreported development
4. Any new retailers who have announced partnerships or agreements with AI companies or announced they are building agentic commerce capabilities.

Be specific. Cite sources.
"""

def synthesis_prompt(agent_results):
    return f'''
You are an editorial director synthesizing research from multiple AI analyst agents.

Topic: "{TOPIC}"
Week of: {datetime.now().strftime("%B %d, %Y")}

Below are independent summaries from research agents:

{agent_results}

---

Produce a final **Weekly Intelligence Briefing** with:
- Top Stories
- Key Themes
- Unique Findings
- Consensus vs. Divergence
- Watch Next Week

STRICT RULE: Every claim must have a source or be marked ⚠️ Unverified.
'''
``
