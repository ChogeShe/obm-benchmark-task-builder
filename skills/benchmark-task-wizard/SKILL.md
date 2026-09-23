---
name: benchmark-task-wizard
description: Guide a user from a real work idea, repository, or system to a complete benchmark proposal and delivery package by selecting a benchmark and A/B/C construction type, gathering only missing requirements, optionally using Trae after explicit permission, and validating the result.
metadata:
  version: "0.1.0"
---

# Benchmark task wizard

Use this skill when a user wants to design, author, validate, package, or publish an expert benchmark task, proposal, verifier, or related Skill for the OBM-style workflow.

The goal is a usable, reviewable delivery package. The user may already know the benchmark and construction type, or may only have a vague work problem. Route both cases through the same guided production flow.

## Operating principles

- Start from the user's facts, files, repository, or real work. Do not invent an expert background, source version, metric, or verifier result.
- The user may answer in natural language. Extract structured fields from the answer and ask only for information that cannot be safely inferred.
- Keep the main intake to three rounds: entry and execution mode, branch-specific gaps, then one specification summary and confirmation.
- After the user confirms the specification, finish the package in one pass. Do not reopen the whole questionnaire for a small correction.
- Treat benchmark compatibility, originality, solvability, behavioral verification, environment limits, and leakage control as release gates.
- The supplied delivery rule says the natural-language fields of `proposal.json` must be human-authored and not AI-generated. Ask the expert to provide their wording. You may outline gaps, critique, and mechanically assemble their text into JSON, but do not silently author or rewrite those fields as final deliverables. If human wording is missing, deliver a clearly marked draft for the expert to replace, not a submission-ready proposal.
- Never put a particular project, dataset, fixed path, hidden test, or expected score into this reusable Skill.

## Round 1: choose a starting mode and execution scope

Ask the user to choose one starting mode, or infer it from an already specific request:

1. **Known direction**: the user already knows the benchmark, source, and possibly A/B/C.
2. **Existing material**: the user has a repository, software, data, or work folder and wants a recommendation.
3. **Work problem**: the user has a real work scenario but no benchmark mapping.

Ask for a compact description of the source material or work problem. If a local path or repository is supplied, inspect it read-only before asking for facts already present in the files.

Ask for the execution mode in the same round:

- generate documents and package only;
- generate and validate locally with terminal/Docker;
- generate and run the workflow in Trae;
- do all available steps.

If Trae, external applications, or file mutation are selected, request explicit permission immediately before those actions. Keep permission scopes separate: read workspace, write files, run terminal/Docker, network access, run no-Skill/with-Skill experiments, and package or push to GitHub. Do not assume a Trae CLI exists. Use a connected UI automation surface when available; otherwise provide executable local steps.

## Round 2: route and ask only branch-specific questions

If the user has not chosen a benchmark or construction type, analyze the material against the official benchmark capability and the A/B/C definitions. Score candidate plans by capability fit, originality, behavioral verifiability, implementation feasibility, difficulty, and delivery cost. Recommend one plan with reasons. If several plans remain materially different, show the short comparison and ask for one choice.

Use the branch guides in [references/abc-guides.md](references/abc-guides.md) and the benchmark constraints in [references/benchmark-matrix.md](references/benchmark-matrix.md).

The minimum hard facts are:

- **A**: a pinned repository/source version, an original new requirement, preserved behavior or interface constraints, and a behavioral verification route;
- **B**: a pinned system or baseline, a new objective, correctness and/or performance metrics, workloads, resource limits, and an anti-cheating verification route;
- **C**: a real expert workflow, concrete inputs and outputs, a programmable acceptance rule, and the expert knowledge that makes the task solvable.

Collect the universal fields from [references/intake-questionnaire.md](references/intake-questionnaire.md): benchmark, domain, related question or capability reference, network policy, environment, task goal, constraints, deliverables, and source inventory.

Block generation only for a hard missing fact. For optional details, choose a conservative default, record the assumption, and show it in the specification summary.

## Round 3: confirm one normalized specification

Before writing the final package, show one concise summary containing:

- selected benchmark and why it fits;
- A/B/C type and why it fits;
- source and pinned version;
- Agent task, inputs, outputs, and constraints;
- task difficulties;
- verifier strategy and hidden-workload plan;
- Skill topics;
- execution permissions and environment;
- assumptions, risks, and unresolved blockers;
- a requirements trace from user facts to proposal, instruction, Skill, verifier, and files.

Ask for one overall confirmation. If the user's answers are already explicit and there is no material ambiguity, proceed without an extra confirmation. Do not start external writes or Trae execution until the relevant permission has been granted.

## Generate the package

After confirmation, build the working materials and the release package in one pass. At minimum, create or specify the release package:

```text
<benchmark>_<proposal-name>/
├── proposal.json
└── sources/
    ├── README.md
    └── ...
```

For an implemented task, keep the authoring workspace's environment, public instruction, source or starter, verifier, hidden-workload generator, reference solution, Skill, and validation records organized separately. Copy into `sources/` only the resources relevant to the proposal and verifier, with a README explaining their uses. Do not automatically submit task prompts, Harbor output, trajectories, or unrelated authoring evidence. Use [references/output-schema.md](references/output-schema.md) for fields and naming.

Keep these artifacts independent:

- proposal explains the task and why it matters;
- instruction exposes the Agent contract and constraints;
- Skill teaches transferable expert reasoning without test or answer leakage;
- verifier checks observable behavior, correctness, and any declared metric;
- source files provide the reproducible environment.

## Quality gates before delivery

Run the checks in [references/quality-gates.md](references/quality-gates.md). At minimum:

1. Validate proposal fields and allowed benchmark/type values.
2. Check the selected benchmark's language, network, OS, GPU, and category constraints.
3. Check originality by recording the sources searched, search terms or identifiers,
   and the conclusion about public-solution risk. Do not claim absolute originality;
   flag unresolved risk for human review.
4. Check that verifier behavior is independent of the implementation and covers hidden variation.
5. Trace every stated difficulty to both Skill guidance and verifier behavior.
6. Search generated prose for invented facts, answer leakage, fixed-workload assumptions, and unresolved placeholders.
7. When the selected execution mode and available environment authorize it, run
   syntax, packaging, local task, determinism, and relevant adversarial checks.
   If an environment, permission, source, or external application is unavailable,
   mark that check as not run and provide the exact command or next action instead
   of implying that it passed.
8. Produce a manifest of the final files and the exact validation commands and results.

If a hard gate fails, report the concrete blocker and fix it before packaging. Do not claim a test passed without running it.

## Prose polishing with Humanizer

The bundled `skills/humanizer/SKILL.md` is available as a separate Skill. Use it when prose polishing is requested or materially improves an eligible authoring document such as a README or an explanatory instruction. Do not use it to disguise AI-authored text as human-authored proposal fields or expert experience. Preserve facts, technical terms, JSON, code, test logic, paths, identifiers, URLs, and numeric constraints exactly. Never use Humanizer to rewrite source code, verifier logic, structured JSON semantics, hidden workloads, or acceptance conditions.

If the companion Skill is unavailable in another installation, use the same no-fabrication and factual-preservation rules without treating Humanizer as a hard dependency. See [references/humanizer-integration.md](references/humanizer-integration.md).

## Optional Trae execution

When the user authorizes Trae, use it as an execution and validation surface, not as an assumed dependency. Work in an isolated copy when possible, record the workspace and permission scope, and preserve the original files. Open the project, inspect the task, run the Agent or validation workflow requested by the user, save relevant outputs, and report the exact files and results. See [references/trae-execution.md](references/trae-execution.md).

## Optional GitHub release

When the user explicitly requests GitHub publication, show the target repository, visibility, branch, files, and diff before pushing. Do not guess a repository, force-push, include credentials, local traces, personal data, or unrelated benchmark artifacts. Run the package and secret scan first, commit only the intended skill bundle, then push to the confirmed remote. See [references/github-release.md](references/github-release.md).
