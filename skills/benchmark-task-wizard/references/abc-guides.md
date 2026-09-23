# A/B/C construction guide

## A: existing or new repository plus a new requirement

Use A when the Agent must modify a codebase to implement an original feature, complex defect repair, migration, refactor, or CI behavior. First classify the requested behavior as absent, currently incorrect, or being migrated; that distinction determines the regression and compatibility checks. Pin the source version and record the URL or local provenance. The new requirement must be authored for the task and must not be reconstructed from a public commit, pull request, or existing solution.

The verifier should exercise observable behavior, compatibility, error handling, and hidden configurations. Existing tests may be a regression layer, but they are not sufficient by themselves.

## B: existing system plus a new objective

Use B when the starting system already works and the task is to achieve a new measurable objective such as latency, throughput, memory, quality, robustness, reimplementation parity, or compiler output. “Make it better” or “more robust” is not enough: pin the baseline, state what already works, and define a numeric or otherwise observable target, workload, metric, resource budget, measurement protocol, and anti-cheating controls before asking an Agent to optimize it.

The verifier should separate semantic correctness from the objective metric. Use hidden workloads and controlled repetitions where variance matters. A candidate that is fast but wrong does not pass; a candidate that is correct but misses the declared objective does not pass either.

## C: real expert work

Use C when the task comes from a real professional workflow and can be turned into a reproducible, programmatically checked coding task. Capture the actual environment, inputs, outputs, expert decisions, and acceptance rule. Do not replace the expert's experience with a generic coding checklist.

## Recommendation rubric

When the user has not chosen a type, score each viable type on:

- capability fit;
- originality and public-solution risk;
- independent verifiability;
- available source and data;
- environment feasibility;
- challenge level;
- delivery cost and deadline risk.

Recommend the highest-scoring option and expose the assumptions. Let the user override the recommendation.
