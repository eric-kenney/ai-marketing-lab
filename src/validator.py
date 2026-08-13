import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from context_builder import LaunchContext

load_dotenv()

client = OpenAI()


def load_validator_prompt() -> str:
    """Load the shared validator prompt."""
    repo_root = Path(__file__).resolve().parent.parent
    prompt_path = repo_root / "prompts" / "validator.md"

    with prompt_path.open("r", encoding="utf-8") as f:
        return f.read()


def validate_asset(
    context: LaunchContext,
    asset: str,
) -> str:
    """
    Review a generated launch asset against the approved
    launch inputs and PMM quality standards.
    """

    model = os.getenv("OPENAI_MODEL", "gpt-5")
    validator_prompt = load_validator_prompt()

    response = client.responses.create(
        model=model,
        instructions=validator_prompt,
        input=f"""
# APPROVED SOURCE MATERIALS

## Product Brief

{context.product_brief}

## Launch Strategy

{context.launch_strategy}

## Launch Plan

{context.launch_plan}

# ASSET TO REVIEW

{asset}
""",
    )

    review = response.output_text.strip()

    if not review:
        raise ValueError("OpenAI returned an empty validation review.")

    return review