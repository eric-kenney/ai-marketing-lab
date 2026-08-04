import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from context_builder import LaunchContext

load_dotenv()

client = OpenAI()


def load_prompt(prompt_name: str) -> str:
    """Load a prompt from the prompts directory."""
    repo_root = Path(__file__).resolve().parent.parent.parent
    prompt_path = repo_root / "prompts" / prompt_name

    with prompt_path.open("r", encoding="utf-8") as f:
        return f.read()


def generate_messaging_framework(context: LaunchContext) -> str:
    model = os.getenv("OPENAI_MODEL", "gpt-5")

    system_prompt = load_prompt("system.md")
    asset_prompt = load_prompt("messaging-framework.md")

    response = client.responses.create(
        model=model,
        instructions=system_prompt,
        input=f"""
{asset_prompt}

# PRODUCT BRIEF

{context.product_brief}

# LAUNCH STRATEGY

{context.launch_strategy}

# LAUNCH PLAN

{context.launch_plan}
""",
    )

    return response.output_text.strip()