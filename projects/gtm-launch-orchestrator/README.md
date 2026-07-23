# AI GTM Launch Orchestrator

An AI-powered operating system for product launches.

The AI GTM Launch Orchestrator transforms a structured product brief into a coordinated set of go-to-market deliverables through a single messaging strategy.

Instead of generating each asset independently, the system creates one strategic foundation that every downstream deliverable inherits.

---

## Why This Exists

Launching enterprise software requires dozens of deliverables across product marketing, sales enablement, content marketing, and field readiness.

Most teams recreate the same messaging repeatedly in different formats.

The AI GTM Launch Orchestrator eliminates that duplication by generating a shared messaging strategy once, then using it to produce a complete launch package.

The goal is faster execution, more consistent messaging, and higher-quality launch assets.

---

## Workflow

```text
                Product Marketer
                       │
                       ▼
              Structured Intake
                       │
                       ▼
              Strategy Model
                       │
                       ▼
        Messaging Source Document
          ┌─────────┼──────────┐
          ▼         ▼          ▼
        ICP     Data Sheet   Pitch Deck
                     │
                     ▼
                 Blog Post
                     │
                     ▼
                 Human Review
```

---

## Features

- Structured launch intake
- Strategy model generation
- Messaging source document
- Ideal Customer Profile generation
- Product data sheet generation
- Sales pitch deck generation
- Launch blog generation
- Human review workflow

---

## Deliverables

The public version generates:

| Deliverable | Purpose |
|-------------|----------|
| Messaging Source Document | Strategic source of truth |
| Ideal Customer Profile | Define the target customer |
| Product Data Sheet | Customer-facing product overview |
| Sales Pitch Deck | Enable sales conversations |
| Launch Blog | Product announcement content |

---

## Architecture

The application separates launch generation into four layers.

```
User Input
      │
      ▼
Structured Intake
      │
      ▼
Strategy Model
      │
      ▼
Deliverable Generators
      │
      ▼
Markdown Outputs
```

This separation allows every deliverable to share the same messaging strategy instead of independently generating content.

---

## Technology

- Python
- Streamlit
- Claude API
- Markdown
- JSON
- GitHub

---

## Repository Structure

```
projects/
└── gtm-launch-orchestrator/
    ├── docs/
    ├── prompts/
    ├── examples/
    ├── assets/
    ├── app.py
    └── README.md
```

---

## Roadmap

- [x] System architecture
- [x] Intake schema
- [x] Strategy model
- [x] Messaging source document
- [ ] Streamlit application
- [ ] AI generation pipeline
- [ ] Deliverable rendering
- [ ] Sample launch project
- [ ] Docker deployment

---

## Design Principles

The orchestrator follows five principles.

- One source of truth
- Structured inputs before generation
- Human review before publication
- Reusable messaging across every asset
- Automation supports strategic decision-making rather than replacing it

---

## License

MIT