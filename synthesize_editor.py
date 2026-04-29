import os
import anthropic
from prompts import synthesis_prompt

def run_editor():
    with open("research_outputs.txt", "r") as f:
        research_text = f.read()

    client = anthropic.Anthropic(
        api_key=os.getenv("ANTHROPIC_API_KEY")
    )

    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=3000,
        messages=[
            {"role": "user", "content": synthesis_prompt(research_text)}
        ]
    )

    return response.content[0].text

if __name__ == "__main__":
    print("Running editorial synthesis agent...")

    output = run_editor()

    with open("weekly_intelligence_brief.md", "w") as f:
        f.write(output)

    print("Weekly intelligence brief created.")
