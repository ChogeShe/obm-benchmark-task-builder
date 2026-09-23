# Optional Trae execution

Trae is an optional execution surface. The Skill must describe its capability honestly: a connected UI automation surface may be available, while a Trae command-line interface may not be.

## Permission scope

Before opening or changing Trae, request one explicit scope covering the actions the user selected:

- read the named workspace;
- create or modify files in that workspace;
- run terminal commands or Docker;
- use network access;
- run a no-Skill and/or with-Skill Agent experiment;
- save logs, patches, traces, and output archives.

If the user declines, continue with file generation and provide commands for manual execution. Never silently replace the UI run with a different external action.

## Execution pattern

1. Use an isolated copy of the workspace when possible.
2. Record the workspace path, permission scope, source hashes, and selected execution mode.
3. Open the workspace in Trae and inspect the public task files.
4. Run the requested Agent or validation workflow.
5. Preserve output, exit code, patch, logs, and test summaries.
6. Run the independent verifier outside the Agent's view when the environment supports it.
7. Report exact paths and limitations. Do not reconstruct missing UI events or claim a trace contains command output when it does not.
