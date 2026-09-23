# OBM Benchmark Task Builder

An installable Codex plugin for turning a real work problem, repository, or software system into a validated benchmark task package.

The main `benchmark-task-wizard` Skill is interactive. It can:

- ask the user to choose a benchmark and A/B/C construction type;
- analyze an idea or workspace and recommend a benchmark/type;
- gather only the missing requirements;
- produce a proposal, public task contract, Skill, verifier plan, sources layout, and validation checklist;
- optionally use Trae after explicit permission;
- use the bundled Humanizer Skill as a separate, optional prose editor;
- validate and package the result for delivery or GitHub publication.

## Included Skills

- `skills/benchmark-task-wizard/` — the OBM task production wizard.
- `skills/humanizer/` — vendored from [blader/humanizer](https://github.com/blader/humanizer), version 2.9.1, MIT licensed. It is an optional prose editor and remains a separate Skill.

## Install from GitHub

```bash
git clone https://github.com/ChogeShe/obm-benchmark-task-builder.git
```

Point Codex or another compatible Agent Skills host at the `skills/` directory, or install the plugin using the host's GitHub/plugin workflow.

## Usage

Ask for a guided production run, for example:

```text
Help me turn my real work problem into a benchmark task package. First ask whether I already know the benchmark and A/B/C type. If not, inspect the material I provide, recommend a plan, ask only the missing questions, and finish the package after one confirmation.
```

The wizard can produce files locally. It asks for explicit permission before opening Trae, changing an external workspace, running an Agent experiment, or pushing to GitHub.

## Validation

From the repository root:

```bash
python3 scripts/validate_package.py .
(cd skills/humanizer && python3 scripts/validate-package.py)
```

The first command is dependency-free and checks the public bundle for structure, placeholders, third-party attribution, and common secret files. The second validates the vendored Humanizer package.
