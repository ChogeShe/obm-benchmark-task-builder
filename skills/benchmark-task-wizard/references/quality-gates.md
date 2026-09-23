# Quality gates

## First delivery gate

- required proposal fields parse and use allowed values;
- benchmark, domain, related question, and language constraints are compatible;
- A/B/C type matches the source and Agent task;
- source files and README are present and understandable;
- task has a plausible solution and a behavioral verification route;
- package contains no credentials, private data, caches, or unrelated artifacts;
- public CLI, Docker, file, and output contracts are internally consistent.

## Internal quality gate

The first delivery gate may be separate from later internal evaluation. A later evaluator may transform the proposal into a benchmark task and compare no-Skill and with-Skill runs. Keep the Skill useful without relying on hidden answers, and preserve evidence of what it teaches. Do not claim a quality bonus or an Agent improvement until that experiment is actually run.

## Evidence status

For every check, record one of `passed`, `failed`, `not run`, or `not applicable`,
along with the command, input/source, and a short result. A missing permission,
unavailable environment, or absent source is a reason to mark a check `not run`,
not a reason to infer success. Originality is an evidence-backed risk assessment,
not an absolute guarantee: preserve the searches and identifiers used so a reviewer
can repeat them.

## Red-team checks

Try to break the proposal with:

- public-search or existing-commit reconstruction;
- visible-name or fixed-count hardcoding;
- input reorder and workspace relocation;
- empty, malformed, boundary, and unexpected-size inputs;
- missing or inconsistent source artifacts;
- a correct implementation that follows a different valid design;
- a Skill that reveals test cases, expected scores, or verifier branches.

## Traceability check

Every stated task difficulty should appear as useful expert guidance in the Skill and as an observable check in the verifier. Every verifier check should be justified by the public contract or a clearly documented robustness requirement.
