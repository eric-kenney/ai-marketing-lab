# Enterprise Product Launch Example

This example demonstrates the AI GTM Launch Orchestrator using **Atlas Knowledge**, a fictional enterprise AI knowledge platform.

The goal is to show the complete workflow: structured launch strategy goes in, multiple GTM assets come out, and each generated asset is independently reviewed against the original source material.

> **Fictional Example**
>
> Atlas Knowledge and all associated product information, claims, launch materials, and generated outputs were created specifically for this repository.

## The Product

Atlas Knowledge is a fictional enterprise knowledge platform designed to help employees find accurate answers across company documentation, collaboration tools, and business applications.

The product uses enterprise search and generative AI to provide concise answers grounded in approved company content, with citations back to the original sources and respect for existing user permissions.

## 1. Start With Strategy

The orchestrator begins with three human-defined source documents:

- [`product-brief.md`](inputs/product-brief.md) — defines the product, customer problem, target audiences, capabilities, success metrics, risks, and assumptions
- [`launch-strategy.md`](inputs/launch-strategy.md) — defines positioning, messaging pillars, differentiation, claims, and strategic guardrails
- [`launch-plan.md`](inputs/launch-plan.md) — defines launch objectives, audiences, deliverables, channels, and execution priorities

These inputs are loaded into a shared `LaunchContext` and remain the source of truth for every generated asset.

Generated assets do not become source material for other generators.

## 2. Generate Multiple GTM Assets

The same strategic context powers three specialized generators.

### Messaging Framework

[`messaging-framework.md`](outputs/messaging-framework.md)

Transforms the launch strategy into a structured messaging system including positioning, messaging pillars, audience messaging, differentiation, claims, and guardrails.

### Sales Battlecard

[`sales-battlecard.md`](outputs/sales-battlecard.md)

Translates the strategy into seller-ready discovery questions, talk tracks, objection handling, competitive positioning, audience plays, qualification guidance, and seller guardrails.

### Product Webpage

[`product-webpage.md`](outputs/product-webpage.md)

Turns the strategy into customer-facing webpage copy covering the problem, value proposition, benefits, product experience, enterprise trust, differentiation, audiences, and calls to action.

## 3. Validate Every Output

Each generated asset is sent through a separate validation step.

The validator compares the generated work against the original product brief, launch strategy, and launch plan rather than evaluating the copy in isolation.

It reviews:

- Strategic alignment
- Differentiation
- Evidence and unsupported claims
- Writing quality
- Audience alignment
- Completeness

The resulting reviews are available here:

- [`messaging-framework-review.md`](outputs/messaging-framework-review.md)
- [`sales-battlecard-review.md`](outputs/sales-battlecard-review.md)
- [`product-webpage-review.md`](outputs/product-webpage-review.md)

## What the Validator Catches

The generated work is intentionally not treated as automatically correct.

For example, the sales battlecard generated the phrase:

> "No content moves."

The approved strategy only supported:

> "No content migration required."

The validator flagged the generated version because it could imply that no indexing, replication, embeddings, or other data movement occurs—something the approved source material does not establish.

It also identified an unsupported reference to what "many customers" do even though the fictional source material contained no customer evidence.

These are small wording differences that can create meaningful claim risk in customer-facing material.

The system surfaces those issues for human review rather than automatically rewriting or approving the asset.

## Why the Workflow Is Structured This Way

The example demonstrates four design choices:

**Strategy remains authoritative.**  
Every generator works from the same approved source material.

**Asset prompts are specialized.**  
A battlecard, messaging framework, and webpage have different jobs even when they share the same strategy.

**Validation is independent from generation.**  
Generated copy is checked against the source material before being considered complete.

**Humans retain approval authority.**  
The validator recommends action but does not silently modify or publish generated work.

## Workflow

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

The result is one launch strategy expressed across multiple GTM deliverables while maintaining a common source of truth and an explicit human-review step.