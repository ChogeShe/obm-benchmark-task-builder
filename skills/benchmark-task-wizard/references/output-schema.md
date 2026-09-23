# Output schema and package layout

The machine-readable proposal should contain the required fields:

```json
{
  "benchmark": "terminal_bench3|terminal_bench4|programbench|swe_marathon|deepSWE|froniterSWE",
  "domain": "English/domain/path",
  "related_question": "official-or-approved-task-name",
  "proposal_type": "A|B|C",
  "allow_network": true,
  "proposal": {
    "A_modification_idea": "...",
    "B_modification_details": "...",
    "C_agent_task": "...",
    "D_task_difficulties": ["..."]
  },
  "proposal_sources": "...",
  "proposal_scene": "...",
  "proposal_verify": "...",
  "expert_experience_skill": "..."
}
```

The supplied schema spells the last enum `froniterSWE`, while the benchmark's brand name is commonly written FrontierSWE. Preserve the exact spelling required by the active checker and record the mapping in the package README. For type C, omit the modification text only when the delivery rules explicitly allow it and no modification exists. For A and B, include source URL and pinned version or commit where required. The natural-language proposal fields and expert experience must be written by the expert; the assistant may validate, critique gaps, or mechanically assemble the supplied text, but must not silently author submission-ready wording.

The release archive should have one top-level directory containing `proposal.json` and `sources/`. Keep a human-readable `README.md` in `sources/` and describe every source file's purpose. Do not include unrelated task prompts, Harbor data, credentials, local traces, caches, or personal files.
