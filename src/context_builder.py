from dataclasses import dataclass
from pathlib import Path


@dataclass
class LaunchContext:
    product_brief: str
    launch_strategy: str
    launch_plan: str


def read_markdown(path: Path) -> str:
    """Read a markdown file and return its contents."""
    with path.open("r", encoding="utf-8") as f:
        return f.read()


def build_context(input_directory: str) -> LaunchContext:
    """
    Build a LaunchContext from the required input documents.
    """
    input_path = Path(input_directory)

    return LaunchContext(
        product_brief=read_markdown(input_path / "product-brief.md"),
        launch_strategy=read_markdown(input_path / "launch-strategy.md"),
        launch_plan=read_markdown(input_path / "launch-plan.md"),
    )