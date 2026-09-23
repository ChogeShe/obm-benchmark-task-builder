# Humanizer integration

This plugin vendors the portable `humanizer` Skill under `skills/humanizer/`. It is an optional prose pass, not a dependency of the benchmark wizard.

Source and attribution:

- upstream: https://github.com/blader/humanizer
- version: 2.9.1
- license: MIT
- preserve the bundled `LICENSE`, `README.md`, and `SKILL.md`.

Use it only after the user facts and structured artifacts are correct. It may polish prose in README text or instruction explanations. The supplied OBM rule requires human-authored proposal fields and expert experience, so do not run Humanizer over those fields to present AI-written text as human work. It must preserve facts, names, numbers, dates, citations, technical terms, URLs, paths, and requirements. Never run it over code, JSON, CSV, verifier logic, hidden workload data, or machine-readable acceptance conditions.

After polishing, recheck the text for factual preservation and for accidental changes to constraints.
