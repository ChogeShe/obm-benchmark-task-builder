# Intake questionnaire

Use this as an adaptive questionnaire, not a form the user must answer mechanically. Ask the first section in one message. After inspecting supplied materials and the user's answers, ask only the missing branch-specific fields.

## Entry and execution

1. Do you already know the benchmark and A/B/C type? If yes, name them. If no, describe the work problem, repository, software, or data.
2. Should the Skill only generate files, also run local validation, use Trae, or perform all available steps?
3. Which workspace or source paths may be inspected? Which may be changed?
4. Is network access allowed for research or execution? Are Docker, GPU, Windows, or external services involved?

## Universal task facts

- What is the real-world context?
- What should the Agent receive?
- What should the Agent change or produce?
- What counts as success?
- What must remain unchanged?
- What are the input, output, time, memory, language, platform, and dependency constraints?
- Which capability should the task test?
- Which benchmark task or capability is the reference, if known?
- What source files, data, URLs, versions, commits, or licenses are available?
- What expert experience should be preserved in the Skill?

## A-specific fields

- Repository/source URL and exact commit, tag, or version.
- Is the requested behavior new, currently incorrect, or being migrated from an old interface?
- New requirement that did not come from a published commit or pull request.
- Existing interface and regression constraints.
- Expected edge cases and failure behavior.
- Hidden workload variations.
- How an independent verifier can observe success without checking a specific patch.

## B-specific fields

- System, software, compiler, model, or baseline name and pinned version.
- What baseline behavior already works, and what measurable target should improve?
- New objective and why it is useful.
- Correctness metric and performance/quality metric.
- Public and hidden workloads.
- Measurement protocol, resource budget, variance tolerance, and stopping rule.
- Allowed modifications, dependencies, and external access.
- Anti-hardcoding and anti-cheating checks.

## C-specific fields

- The expert's real work process and why it matters.
- Concrete input and output artifacts.
- Decisions that require expert judgment.
- Programmable acceptance and failure cases.
- Environment construction and available source/data.
- Generalizable expert guidance that makes the task solvable.

## Confirmation payload

The final summary should render as a compact decision record, not a long transcript. Include selected values, user-provided facts, assumptions, risks, and the one requirements trace that will govern generation.
