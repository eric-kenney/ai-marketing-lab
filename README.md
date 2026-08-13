# AI Marketing Lab

Applied AI systems for product marketing and go-to-market teams.

## Featured Project: AI GTM Launch Orchestrator

The AI GTM Launch Orchestrator turns approved launch strategy into multiple go-to-market assets while validating the generated work against the original source material.

It uses a shared strategic context to generate a messaging framework, sales battlecard, and product webpage, then independently reviews each asset for strategic alignment, unsupported claims, differentiation, and quality.

> **Portfolio Project**
>
> AI Marketing Lab is a fictional demonstration project created to showcase AI-assisted product marketing workflows. All products, launch materials, messaging, and generated outputs are fictional and do not represent any employer, customer, or confidential information.

## Why This Exists

Product marketing teams don't usually struggle because they lack another writing tool. They struggle to turn strategy into dozens of consistent, accurate launch assets without losing the thinking that made the strategy good in the first place.

AI Marketing Lab explores how LLMs can help solve that problem.

The goal is not to automate product marketing judgment. It is to build systems that take structured strategic inputs, apply consistent product marketing standards, accelerate execution, and preserve human review where judgment matters.

## How It Works

```text
                    ┌─ Messaging Framework ─► Validation ─► Review
                    │
Launch Inputs ──────┼─ Sales Battlecard ─────► Validation ─► Review
                    │
                    └─ Product Webpage ───────► Validation ─► Review
```

The system begins with three structured inputs:

- Product Brief
- Launch Strategy
- Launch Plan

Those inputs are loaded into a shared `LaunchContext` and remain the source of truth throughout the workflow.

Each asset generator combines that context with:

- A shared system prompt defining product marketing standards
- An asset-specific prompt defining the job to be done
- The OpenAI Responses API for generation

Every generated asset then passes through a separate validation step that compares the output against the approved launch inputs.

## What It Generates

### Messaging Framework

Creates positioning, messaging pillars, audience-specific messaging, competitive differentiation, message hierarchy, approved claims, and messaging guardrails.

### Sales Battlecard

Turns the same launch strategy into field-ready discovery questions, talk tracks, objection handling, competitive positioning, audience plays, qualification guidance, proof points, and seller guardrails.

### Product Webpage

Creates customer-facing webpage copy including the hero, problem narrative, value proposition, benefits, product experience, enterprise trust story, differentiation, audience messaging, and calls to action.

The webpage also generates an internal claims check so reviewers can see which claims are supported and which were intentionally excluded.

## Validation and Human Review

Generation is only half of the workflow.

Every asset is independently reviewed against the original launch materials for:

- Strategic alignment
- Differentiation
- Evidence and unsupported claims
- Writing quality
- Audience alignment
- Completeness

The validator produces a score, strengths, prioritized improvements, and an approval recommendation.

This catches issues that can look reasonable in generated copy but are not supported by the source material—for example, turning "no content migration required" into the broader claim "no content moves," or introducing customer behavior without customer evidence.

The validator does **not** automatically rewrite the asset.

That is intentional.

The workflow keeps a human product marketer in the approval loop rather than allowing one model output to silently modify another.

## Architecture

```text
examples/enterprise-product-launch/inputs/
        │
        ▼
   LaunchContext
        │
        ├───────────────┬─────────────────┐
        ▼               ▼                 ▼
   Messaging        Sales            Product
   Generator        Battlecard        Webpage
        │           Generator         Generator
        │               │                 │
        ▼               ▼                 ▼
     Output           Output            Output
        │               │                 │
        └───────────────┼─────────────────┘
                        ▼
                     Validator
                        │
                        ▼
                  Review Outputs
```

The architecture deliberately separates three concerns:

**Strategy**  
The product brief, launch strategy, and launch plan define what is true.

**PMM standards**  
Shared prompt instructions define how the system should reason and write.

**Asset execution**  
Asset-specific prompts define what each generator needs to produce.

This allows new deliverables to use the same strategic context and quality standards without rebuilding the underlying system.

## Repository Structure

```text
ai-marketing-lab/
├── docs/
│
├── examples/
│   └── enterprise-product-launch/
│       ├── inputs/
│       └── outputs/
│
├── prompts/
│   ├── system.md
│   ├── messaging-framework.md
│   ├── sales-battlecard.md
│   ├── product-webpage.md
│   └── validator.md
│
├── src/
│   ├── generators/
│   │   ├── messaging_framework.py
│   │   ├── sales_battlecard.py
│   │   └── product_webpage.py
│   ├── context_builder.py
│   ├── orchestrator.py
│   └── validator.py
│
├── tests/
├── requirements.txt
└── README.md
```

## Running the Orchestrator

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file containing your OpenAI API configuration:

```text
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=gpt-5
```

Run:

```bash
python3 src/orchestrator.py
```

The orchestrator loads the launch inputs, generates all three assets, validates each one, and writes the assets and reviews to:

```text
examples/enterprise-product-launch/outputs/
```

## Design Principles

### Strategy remains the source of truth

Generated assets are derived from approved launch inputs rather than from other generated assets. This reduces the risk of errors compounding across the content chain.

### Prompts and code have different jobs

Python handles orchestration. Markdown prompt files define PMM reasoning standards and asset requirements. Prompt quality can therefore evolve without changing application logic.

### Claims require evidence

The system is instructed not to invent capabilities, integrations, customer evidence, pricing, performance results, or proof points that aren't supported by the source material.

### Generation requires validation

A plausible answer is not necessarily an approved answer. Generated work is checked against the strategy before it is considered complete.

### Humans retain judgment

The validator identifies problems and recommends action. It does not automatically approve or rewrite customer-facing work.

## Technology

- Python
- OpenAI Responses API
- Markdown-based prompt architecture
- Structured launch context
- Environment-based model configuration
- Git/GitHub

## Current Status

The core orchestration workflow is complete.

The current implementation demonstrates one launch context powering three distinct product marketing deliverables, with independent validation and human review built into the workflow.

Future experiments in AI Marketing Lab may explore competitive intelligence, business-value modeling, and other product marketing workflows.