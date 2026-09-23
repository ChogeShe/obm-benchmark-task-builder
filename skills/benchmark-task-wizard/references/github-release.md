# GitHub release workflow

Use this workflow only when the user explicitly asks for publication.

1. Scan the intended repository tree for credentials, API keys, private data, benchmark traces, caches, `.DS_Store`, and unrelated task artifacts.
2. Show the repository URL or proposed name, visibility, branch, file list, and diff.
3. Confirm the remote and branch before the first push if they were not explicitly supplied.
4. Validate the plugin manifest, each Skill, and the bundle manifest locally.
5. Initialize Git if needed, stage only the intended files, commit with a descriptive message, and push through the authenticated GitHub client.
6. Never force-push or overwrite an existing remote without explicit instruction.
7. Return the GitHub URL, commit, branch, and local package path.
