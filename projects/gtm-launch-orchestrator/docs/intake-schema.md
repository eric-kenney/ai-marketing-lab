# Intake Schema

## Overview

The orchestrator begins with a structured intake rather than an open-ended prompt.

The intake captures the strategic inputs required to create a credible launch package. It also reduces the likelihood that the model will invent missing information or produce inconsistent messaging across deliverables.

Fields are organized into eight sections:

1. Product Basics
2. Customer Problem
3. Positioning
4. Target Audience
5. Proof
6. Pricing and Sales
7. Competitive Context
8. Launch Details

---

## 1. Product Basics

### Product Name

**Required:** Yes

The public-facing name of the product, feature, or service being launched.

**Used by:** All deliverables

### One-Line Description

**Required:** Yes

A concise explanation of what the product does and who it is for.

**Used by:** Messaging Source Document, Data Sheet, Pitch Deck, Blog Post

### Product Category

**Required:** Yes

The category or market in which the product competes.

Examples:

- Customer support software
- Revenue intelligence
- Cybersecurity
- Collaboration software

**Used by:** Messaging Source Document, Ideal Customer Profile, Pitch Deck

### Release State

**Required:** Yes

The current stage of the product.

Suggested values:

- Concept
- Private beta
- Public beta
- General availability
- Major enhancement

**Used by:** Messaging Source Document, Blog Post, Pitch Deck

---

## 2. Customer Problem

### Primary Customer Problem

**Required:** Yes

The most important problem the product is designed to solve.

**Used by:** All deliverables

### Current Consequences

**Required:** Yes

The business or operational impact of leaving the problem unresolved.

Examples:

- Lost revenue
- Higher operating costs
- Slower response times
- Increased risk
- Poor customer experience

**Used by:** Messaging Source Document, Data Sheet, Pitch Deck, Blog Post

### Existing Workarounds

**Required:** No

How customers currently address the problem without this product.

**Used by:** Messaging Source Document, Pitch Deck, Blog Post

---

## 3. Positioning

### Primary Outcome

**Required:** Yes

The most important result the product enables.

**Used by:** All deliverables

### Why Now

**Required:** Yes

The market, customer, or technology change that makes the product timely.

**Used by:** Messaging Source Document, Pitch Deck, Blog Post

### Differentiators

**Required:** Yes

The capabilities, design choices, or advantages that distinguish the product from customer alternatives.

Differentiators should explain why the product is meaningfully different, not simply list standard features.

**Used by:** Messaging Source Document, Data Sheet, Pitch Deck

### Value Proposition

**Required:** No

An initial statement explaining why the target customer should choose the product.

The system may refine this statement during generation.

**Used by:** Messaging Source Document, Data Sheet, Pitch Deck

### Positioning Statement

**Required:** No

A structured statement defining the target customer, the category, the primary value, and the reason the product is different.

The system may generate or refine this statement from the other intake fields.

**Used by:** Messaging Source Document, Data Sheet, Pitch Deck

### Messaging Pillars

**Required:** No

The three to five core themes that should appear consistently across launch materials.

Each pillar should connect a customer need, product capability, and business outcome.

**Used by:** All deliverables

### Reasons to Believe

**Required:** No

The product capabilities, evidence, or design choices that make the value proposition credible.

Examples:

- Proprietary technology
- Workflow integration
- Customer results
- Performance benchmarks
- Security or compliance capabilities

**Used by:** Messaging Source Document, Data Sheet, Pitch Deck, Blog Post

### Message Guardrails

**Required:** No

Claims, phrases, topics, or positioning approaches that should be avoided.

Examples:

- Unsupported superlatives
- Competitive claims that have not been validated
- Features that are not generally available
- Language that creates legal or compliance risk

**Used by:** All deliverables

---

## 4. Target Audience

### Primary Buyer

**Required:** Yes

The person most likely to approve or fund the purchase.

**Used by:** Messaging Source Document, Ideal Customer Profile, Pitch Deck

### Primary User

**Required:** Yes

The person most likely to use the product regularly.

**Used by:** Messaging Source Document, Ideal Customer Profile, Data Sheet

### Company Size

**Required:** No

The customer segments most likely to benefit.

Suggested values:

- Small business
- Mid-market
- Enterprise

**Used by:** Ideal Customer Profile, Pitch Deck

### Priority Industries

**Required:** No

Industries where the problem is especially urgent or the product has a strong fit.

**Used by:** Ideal Customer Profile, Pitch Deck, Blog Post

### Geography

**Required:** No

The regions where the product is available or most relevant.

**Used by:** Ideal Customer Profile, Blog Post

---

## 5. Proof

### Supporting Metrics

**Required:** No

Quantitative evidence supporting the product's value.

Examples:

- Time saved
- Cost reduction
- Revenue improvement
- Adoption rate
- Accuracy improvement

**Used by:** Messaging Source Document, Data Sheet, Pitch Deck, Blog Post

### Customer Evidence

**Required:** No

Customer quotes, pilot feedback, case-study evidence, or observed results.

**Used by:** Data Sheet, Pitch Deck, Blog Post

### External Validation

**Required:** No

Relevant analyst findings, market research, certifications, or third-party validation.

**Used by:** Messaging Source Document, Pitch Deck, Blog Post

---

## 6. Pricing and Sales

### Pricing Model

**Required:** No

How the product is packaged and sold.

Examples:

- Per user
- Usage based
- Flat-rate subscription
- Add-on
- Custom enterprise pricing

**Used by:** Messaging Source Document, Data Sheet, Pitch Deck

### Sales Motion

**Required:** No

How customers are expected to purchase the product.

Suggested values:

- Self-service
- Product-led
- Sales-assisted
- Enterprise sales

**Used by:** Ideal Customer Profile, Pitch Deck

### Common Objections

**Required:** No

The concerns buyers or users may raise during evaluation.

**Used by:** Messaging Source Document, Pitch Deck

---

## 7. Competitive Context

### Primary Alternatives

**Required:** No

The products, vendors, internal processes, or manual approaches customers may consider instead.

**Used by:** Messaging Source Document, Pitch Deck

### Competitive Advantages

**Required:** No

The most important reasons the product is better suited to the target customer than those alternatives.

**Used by:** Messaging Source Document, Data Sheet, Pitch Deck

---

## 8. Launch Details

### Launch Tier

**Required:** Yes

The strategic importance and level of support required for the launch.

Suggested values:

- Tier 1: Major product or market launch
- Tier 2: Significant feature or expansion
- Tier 3: Incremental enhancement

**Used by:** Workflow configuration

### Launch Objective

**Required:** Yes

The primary business result the launch is expected to produce.

Examples:

- Generate pipeline
- Drive adoption
- Enter a new market
- Increase retention
- Support expansion revenue

**Used by:** Messaging Source Document, Pitch Deck, Blog Post

### Launch Date

**Required:** No

The planned release or announcement date.

**Used by:** Blog Post, workflow planning

### Supporting Materials

**Required:** No

Links or references to relevant research, product documentation, customer interviews, or other source material.

**Used by:** All deliverables

---

## Validation Rules

Before generation begins, the system should confirm that:

- All required fields are complete
- The customer problem is specific
- The primary outcome is measurable or observable
- Differentiators are distinct from basic product features
- Buyer and user roles are not treated as interchangeable
- Claims are supported by evidence when evidence is provided
- Missing information is identified rather than invented

---

## Design Principle

The intake should capture strategy without becoming so burdensome that product marketers avoid using it.

The goal is not to collect every possible fact. It is to gather the minimum set of inputs required to generate useful, consistent, and reviewable launch materials.