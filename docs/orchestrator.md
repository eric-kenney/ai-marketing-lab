# GTM Launch Orchestrator

## Purpose

The GTM Launch Orchestrator is the execution layer of AI Marketing Lab. It transforms a small set of approved product marketing inputs into consistent go-to-market assets and independently reviews those assets against the original strategy.

The orchestrator reads the product brief, launch strategy, and launch plan for a specific launch. Those inputs establish a shared strategic context used by each asset generator.

The goal is not to replace product marketing judgment. The goal is to make approved strategy reusable, reduce repetitive execution, improve consistency across deliverables, and surface potential quality or claim issues for human review.

## Inputs

Every orchestration begins with three required inputs:

| Input | Purpose |
| --- | --- |
| Product Brief | Defines the product, customer problem, target users, capabilities, business objectives, risks, and assumptions. |
| Launch Strategy | Defines positioning, messaging pillars, differentiation, proof points, and strategic guardrails. |
| Launch Plan | Defines launch objectives, audiences, deliverables, channels, dependencies, risks, and success metrics. |

Together, these documents establish the approved strategy for a launch.

They remain the source of truth throughout the workflow. Generated assets are not used as source material for subsequent generators.

## Current Outputs

The current implementation generates three assets:

- Messaging Framework
- Sales Battlecard
- Product Webpage

Each asset is generated independently from the same shared launch context.

The architecture is designed so additional asset generators can be added while reusing the same inputs, shared product marketing standards, and validation workflow.

## Orchestration Workflow

```text
Product Brief ──────┐
Launch Strategy ────┼──► LaunchContext
Launch Plan ────────┘         │
                              │
                 ┌────────────┼────────────┐
                 ▼            ▼            ▼
             Messaging      Sales       Product
             Framework    Battlecard    Webpage
                 │            │            │
                 ▼            ▼            ▼
              Validate     Validate     Validate
                 │            │            │
                 ▼            ▼            ▼
               Review       Review       Review
```

A single orchestrator run currently:

1. Loads the three launch inputs.
2. Builds a shared `LaunchContext`.
3. Generates the messaging framework.
4. Reviews the messaging framework against the source material.
5. Generates the sales battlecard.
6. Reviews the sales battlecard against the source material.
7. Generates the product webpage.
8. Reviews the product webpage against the source material.
9. Writes all generated assets and reviews to the example output directory.

## Prompt Architecture

The system separates shared product marketing standards from asset-specific instructions.

The shared system prompt defines how the model should reason and write across deliverables.

Asset-specific prompts define the requirements for:

- Messaging frameworks
- Sales battlecards
- Product webpages

This keeps orchestration logic in Python while allowing product marketing requirements and prompt instructions to evolve independently from the application code.

## Validation

Every generated asset passes through the same reusable validator.

The validator receives:

- The original Product Brief
- The original Launch Strategy
- The original Launch Plan
- The generated asset

It evaluates the asset for:

- Strategic alignment
- Differentiation
- Evidence and unsupported claims
- Writing quality
- Audience alignment
- Completeness

The validator produces a separate review containing an overall score, strengths, prioritized improvements, and an approval recommendation.

It does not automatically rewrite or approve the generated asset.

This preserves an explicit human-review step.

## Design Principles

The GTM Launch Orchestrator follows five core principles:

1. **Strategy First** — Generated work should apply approved strategy rather than redefine it.

2. **Single Source of Truth** — Every generated asset derives from the same launch inputs rather than from other generated assets.

3. **Modular Generation** — Each asset has its own generator and prompt while sharing the same context and product marketing standards.

4. **Independent Validation** — Generated work is reviewed against its source material rather than assumed to be correct.

5. **Human in the Loop** — Validation surfaces issues and recommends action; a human retains approval authority.

## System Components

| Component | Responsibility |
| --- | --- |
| Context Builder | Loads the approved launch inputs and creates the shared `LaunchContext`. |
| Orchestrator | Coordinates generation, validation, and output creation. |
| Asset Generators | Apply asset-specific prompts to the shared launch context. |
| Validator | Reviews generated assets against the original launch inputs and product marketing quality standards. |
| Prompt Files | Define shared PMM standards, asset requirements, and validation criteria independently from Python code. |

## Extending the System

Adding another deliverable follows the same pattern:

```text
LaunchContext
     │
     ▼
Asset-specific prompt
     │
     ▼
Asset generator
     │
     ▼
Generated output
     │
     ▼
Shared validator
     │
     ▼
Human review
```

A new asset therefore requires specialized generation instructions and a generator, but does not require a new strategic input model or validation architecture.

## Non-Goals

The GTM Launch Orchestrator does not:

- Replace product marketing strategy or decision-making.
- Treat generated content as automatically approved.
- Invent evidence that is absent from the approved source material.
- Publish content directly to external systems.
- Replace human review and approval.
- Serve as a project management or workflow automation platform.

The orchestrator is designed to accelerate execution while keeping strategy, evidence, and approval under human control.