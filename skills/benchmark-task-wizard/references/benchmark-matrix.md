# Benchmark compatibility matrix

Use official benchmark documentation and task metadata when the user asks for a current or exact mapping. Do not invent a `related_question` name or category.

| Benchmark | Typical fit | Constraints to check |
|---|---|---|
| `terminal-bench3` / `terminal-bench4` | Linux terminal coding, debugging, operations, data, and system tasks | Linux runtime, network policy, CPU/memory/time, no unsupported GPU or Windows dependency |
| `programbench` | Program implementation or repair with a language-specific contract | The task language must not be Python; verify the benchmark's current interface |
| `swe_marathon` | Longer software-engineering repair or feature work | Repository state, test/runtime budget, task duration and source provenance |
| `deepSWE` | Deep software-engineering work with multi-file reasoning | Confirm current task format and environment before authoring |
| FrontierSWE (`froniterSWE` in the supplied schema) | Frontier software-engineering capability evaluation | Confirm current task format, environment, and checker enum before authoring |

The user may select a benchmark directly. If the Skill recommends one, explain the capability match and verify the current official task name, domain, and related-question convention before writing them into a deliverable.
