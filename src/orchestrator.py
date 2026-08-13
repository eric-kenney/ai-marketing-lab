from pathlib import Path

from context_builder import build_context
from generators.messaging_framework import generate_messaging_framework
from generators.sales_battlecard import generate_sales_battlecard
from validator import validate_asset

from generators.product_webpage import generate_product_webpage


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent

    input_directory = (
        repo_root
        / "examples"
        / "enterprise-product-launch"
        / "inputs"
    )

    output_directory = (
        repo_root
        / "examples"
        / "enterprise-product-launch"
        / "outputs"
    )

    output_directory.mkdir(parents=True, exist_ok=True)

    print("Loading launch inputs...")
    context = build_context(input_directory)

    # Messaging Framework
    print("Generating messaging framework...")
    messaging_framework = generate_messaging_framework(context)

    messaging_file = output_directory / "messaging-framework.md"
    messaging_file.write_text(
        messaging_framework,
        encoding="utf-8",
    )

    print("Validating messaging framework...")
    messaging_review = validate_asset(
        context,
        messaging_framework,
    )

    messaging_review_file = (
        output_directory / "messaging-framework-review.md"
    )
    messaging_review_file.write_text(
        messaging_review,
        encoding="utf-8",
    )

    # Sales Battlecard
    print("Generating sales battlecard...")
    sales_battlecard = generate_sales_battlecard(context)

    battlecard_file = output_directory / "sales-battlecard.md"
    battlecard_file.write_text(
        sales_battlecard,
        encoding="utf-8",
    )

    print("Validating sales battlecard...")
    battlecard_review = validate_asset(
        context,
        sales_battlecard,
    )

    battlecard_review_file = (
        output_directory / "sales-battlecard-review.md"
    )
    battlecard_review_file.write_text(
        battlecard_review,
        encoding="utf-8",
    )

    # Product Webpage
    print("Generating product webpage...")
    product_webpage = generate_product_webpage(context)

    webpage_file = output_directory / "product-webpage.md"
    webpage_file.write_text(
        product_webpage,
        encoding="utf-8",
    )

    print("Validating product webpage...")
    webpage_review = validate_asset(
        context,
        product_webpage,
    )

    webpage_review_file = (
        output_directory / "product-webpage-review.md"
    )
    webpage_review_file.write_text(
        webpage_review,
        encoding="utf-8",
    )

    print("Done.")
    print(f"Messaging framework: {messaging_file}")
    print(f"Messaging review: {messaging_review_file}")
    print(f"Sales battlecard: {battlecard_file}")
    print(f"Battlecard review: {battlecard_review_file}")
    print(f"Product webpage: {webpage_file}")
    print(f"Webpage review: {webpage_review_file}")


if __name__ == "__main__":
    main()