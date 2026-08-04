from pathlib import Path

from context_builder import build_context
from generators.messaging_framework import generate_messaging_framework


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent

    input_directory = (
        repo_root
        / "examples"
        / "enterprise-product-launch"
        / "inputs"
    )

    output_file = (
        repo_root
        / "examples"
        / "enterprise-product-launch"
        / "outputs"
        / "messaging-framework.md"
    )

    print("Loading launch inputs...")
    context = build_context(input_directory)

    print("Generating messaging framework...")
    messaging_framework = generate_messaging_framework(context)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(messaging_framework, encoding="utf-8")

    print(f"Messaging framework saved to:\n{output_file}")


if __name__ == "__main__":
    main()