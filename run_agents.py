from prompts import AGENT_PROMPT
from openai import OpenAI
import os

def run_agent(model_name):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": AGENT_PROMPT}
        ],
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    print("Running research agent...")

    output = run_agent("gpt-4.1")

    with open("agent_output.txt", "w") as f:
        f.write(output)

    print("Research complete. Output saved to agent_output.txt")
