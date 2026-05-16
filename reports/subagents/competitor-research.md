# Competitor Research: Coding Agent Runtime Interfaces

Research date: 2026-05-16
Role: competitor-researcher

## Task Scope

This report compares public coding agent, CLI, and agent-computer interface designs that are relevant to a model-neutral Codex-style coding runtime MCP server. The focus is not product wrapping or model orchestration. The focus is the low-level runtime surface required by the project: file read, directory/file search, structured edits, shell execution, stdin/session handling, git status/diff, permissions, sandboxing, and how subagents or parallel work are handled.

## Materials Read, Cloned, or Referenced

No large reference repositories were cloned for this subtask. I used primary web documentation and GitHub-hosted docs to avoid committing reference code under `.reference/`.

- OpenCode official docs: tools and agents/permissions: https://opencode.ai/docs/tools/ and https://opencode.ai/docs/agents/
- OpenCode repo referenced from task: https://github.com/anomalyco/opencode
- Claude Code official docs: subagents, MCP, permissions, permission modes, settings, hooks: https://code.claude.com/docs/en/sub-agents, https://code.claude.com/docs/en/mcp, https://code.claude.com/docs/en/permissions, https://code.claude.com/docs/en/permission-modes, https://code.claude.com/docs/en/settings, https://code.claude.com/docs/en/hooks
- Gemini CLI official docs: tools, filesystem tools, shell, checkpointing, sandboxing, MCP servers, subagents: https://google-gemini.github.io/gemini-cli/docs/tools/, https://google-gemini.github.io/gemini-cli/docs/tools/file-system.html, https://google-gemini.github.io/gemini-cli/docs/tools/shell.html, https://google-gemini.github.io/gemini-cli/docs/cli/checkpointing.html, https://google-gemini.github.io/gemini-cli/docs/cli/sandbox.html, https://google-gemini.github.io/gemini-cli/docs/tools/mcp-server.html, https://github.com/google-gemini/gemini-cli/blob/main/docs/core/subagents.md
- Google Developers Blog on Gemini CLI subagents: https://developers.googleblog.com/subagents-have-arrived-in-gemini-cli/
- Aider docs: edit formats, repo map, git integration, commands, lint/test: https://aider.chat/docs/more/edit-formats.html, https://aider.chat/docs/repomap.html, https://aider.chat/docs/git.html, https://aider.chat/docs/usage/commands.html, https://aider.chat/docs/usage/lint-test.html
- SWE-agent docs and paper: https://swe-agent.com/0.7/ and https://arxiv.org/abs/2405.15793
- mini-SWE-agent SWE-bench docs: https://mini-swe-agent.com/latest/usage/swebench/
- MCP tools spec and schema/annotations: https://modelcontextprotocol.io/specification/2025-06-18/server/tools and https://modelcontextprotocol.io/specification/2025-11-25/schema
- MCP Inspector docs and repo: https://modelcontextprotocol.io/docs/tools/inspector and https://github.com/modelcontextprotocol/inspector
- Public analysis referenced: MCP tool annotation risk vocabulary: https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations/

## Key Findings

### Comparative Runtime Surface

| Tool | File read/search | Edit model | Shell and tests | Diff/status | Permissions and sandbox | Subagents/parallel work |
| --- | --- | --- | --- | --- | --- | --- |
| OpenCode | Built-ins include `read`, `list`, `glob`, `grep`, and experimental `lsp`. `read` supports line ranges; `grep` supports regex and file patterns. | `edit` exact string replacement, `write` create/overwrite, and `apply_patch` with project-relative paths embedded in patch markers. | `bash` runs commands in the project environment. | Git workflows are available through shell; patch tool paths are root-relative. | Permission keys gate `read`, `edit`, `glob`, `grep`, `list`, `bash`, `task`, `external_directory`, `lsp`, and MCP tools. Actions are `allow`, `ask`, or `deny`, with command/path patterns. Docs say tools are enabled by default unless configured. | Agents can be configured with per-agent permissions. `task` is the delegation primitive; todo tools are disabled for subagents by default unless enabled. |
| Claude Code | Internal tools include Read/Grep/Glob and file access rules; docs also discuss read-only Bash commands such as `ls`, `cat`, `grep`, `find`, `diff`, and read-only git. | Edit/write tools are governed by permission rules and modes. Plan mode is read-only for source edits. | Bash is a first-class tool. Read-only commands can run without prompts; other commands route through permissions, sandboxing, or auto mode. | `/diff`/skills can inject `git diff`; read-only git and diff commands are recognized. | Richest permission model: allow/ask/deny rules, default/acceptEdits/auto/dontAsk/bypassPermissions/plan modes, protected paths, managed settings, and optional OS-level sandboxing for Bash filesystem/network access. Docs warn Bash rules are not complete OS enforcement. | Subagents have isolated context, model choice, tool allowlist/denylist, scoped MCP servers, scoped hooks, max turns, optional memory, and optional temporary git worktree isolation. Hooks expose SubagentStart/Stop and Task events. |
| Gemini CLI | File tools include `list_directory`, `read_file`, `read_many_files`, `glob`, and `search_file_content`. File tools operate under `rootDirectory`; search uses git grep when available and ignores common nuisance dirs. | `write_file` overwrites/creates with confirmation and diff. `replace` uses exact literal old/new strings, requires strong context, and can attempt model-assisted edit correction. | `run_shell_command` executes via shell, returns stdout/stderr/error/exit code/signal/background PIDs, can use PTY for interactive commands, and supports command restrictions. | Checkpointing stores snapshots before mutating tools in a shadow git repo. Users can restore checkpoints. Git diff can be run through shell. | Confirmation prompts for mutating filesystem/shell actions. Command allow/exclude uses prefix matching and chained-command splitting but docs warn this is not a security mechanism. Sandboxing supports macOS seatbelt and Docker/Podman; profiles can restrict writes and network. MCP servers have `trust`, include/exclude tools, and timeouts. | Subagents are exposed as tools with independent context and specialized tool access. Built-ins include codebase investigator, CLI help, generalist, and browser agent. Browser agent adds domain restrictions, sensitive action confirmation, action limits, and sandbox-specific behavior. |
| Aider | User explicitly adds files; repo map summarizes important symbols across the git repo. `/map`, `/add`, `/read-only`, `/ls` support context control. | Model-specific edit formats: whole file, search/replace blocks, fenced variants, and simplified unified diff. Architect/editor mode splits planning from edit generation. | `/run`, `/test`, and `/lint` execute shell commands and can feed failures back into the chat for repair. | Strong git integration: auto-commits edits, `/diff` shows changes since last message, `/undo` reverts the last aider commit, `/git` exposes raw git. | No comparable sandbox or fine-grained permission system in primary docs. Safety mainly comes from git snapshots/undo and user control over files in chat. | No general subagent system. Architect/editor mode is a two-model division of labor, not parallel worker orchestration. |
| SWE-agent | ACI emphasizes custom commands for search, paginated `open`, `scroll`, `goto`, and repository navigation rather than raw unstructured terminal output. | Line-addressed `edit <file> <start> <end>` replacement. The design avoids ambiguous natural language edits. | Standard Unix tools remain available; benchmark flows execute tests and reproduction scripts. | Final answer is a git patch for SWE-bench; patch review is central. | Runs tasks in controlled benchmark environments, commonly Docker. Security model is benchmark isolation more than reusable local permission prompts. | Original SWE-agent is a single-agent ACI. Parallelism comes from benchmark runners, not agent collaboration. |
| mini-SWE-agent | Simplifies to a bash-centric interface. Instructions encourage search/read with `ls`, `find`, `grep`, `cat`, `head`, `sed`, etc. | Edits are done through shell commands/scripts; final submission must be a `git diff` patch. | One or more bash tool calls per turn; each action runs in a new subshell, with non-persistent directory/env changes unless command-prefixed. Output is capped with head/tail elision. | Explicit patch generation and verification; no commits. | Default SWE-bench config uses Docker environment, `/testbed` cwd, timeout, env sanitizers such as `PAGER=cat`, and output caps. Singularity/Apptainer is supported. | Batch mode runs instances in parallel. The model config can enable parallel tool calls for independent bash commands. |
| MCP Inspector/spec | MCP itself supplies schema-based tool discovery and invocation, not coding primitives. Inspector lists tools, schemas, resources, prompts, notifications, and call results. | Edit behavior is server-defined. MCP tools expose `inputSchema`, optional `outputSchema`, and `CallToolResult`. | Shell behavior is server-defined. Inspector can call tools interactively or from CLI. | Diff/status behavior is server-defined. | Tool annotations such as `readOnlyHint`, `destructiveHint`, `idempotentHint`, and `openWorldHint` are hints, not security guarantees. Clients must not trust annotations from untrusted servers. | MCP has no standard subagent abstraction. Inspector CLI is useful for CI-style `tools/list` and `tools/call` checks. |

### Patterns That Matter For This Project

1. The best coding runtimes expose small, task-shaped primitives instead of only raw shell. OpenCode, Claude Code, and Gemini all provide separate read/search/edit tools. SWE-agent shows that a purpose-built ACI can outperform a generic terminal for software tasks.
2. Shell remains necessary but must be constrained. Claude and Gemini both document the weakness of string/prefix matching for shell safety. A runtime MCP server should enforce workspace and environment limits server-side rather than relying on client prompts or tool annotations.
3. Edits need deterministic semantics. OpenCode's `apply_patch` and Aider's edit formats show why model output should be parsed into a strict edit operation. Gemini's model-assisted edit correction is useful for a product but unsuitable for a deterministic tool runtime contract.
4. Diff visibility is a first-class affordance. Aider's `/diff` and auto-commit undo flow, Gemini checkpointing, and SWE-bench patch submission all reinforce that agents need cheap, structured diff inspection after every edit.
5. Subagents should be an orchestration feature, not a P0 MCP runtime primitive. Claude and Gemini make subagents useful by giving them isolated context, scoped tools, and sometimes worktree isolation. This project should use that pattern for dogfood and internal tests, but not expose "spawn subagent" as an MCP tool.
6. MCP compatibility requires strong schemas and external testability. The Inspector CLI is directly useful for compliance tests because it can call `tools/list` and `tools/call` without a full chat client.

## Concrete Recommendations

1. Implement a narrow P0 MCP tool surface: `read_file`, `list_dir`, `list_files`, `search_text`, `apply_patch`, `exec_command`, `write_stdin`, `kill_session`, `git_status`, `git_diff`, and `request_permissions`. Do not expose product-layer tools such as memory, login, web search, model selection, or subagent spawning.
2. Use workspace-relative paths for public inputs, even though Gemini often documents absolute paths. Canonicalize every path and require it to remain under the configured workspace root after symlink resolution.
3. Borrow OpenCode's permission vocabulary by grouping capabilities as read, edit, bash, external_directory, and MCP/open-world operations. Make the server enforce the groups; use MCP annotations only as descriptive hints.
4. Borrow Claude's defense-in-depth split: declarative permission rules plus OS-level sandboxing for shell as a future enhancement. For P0, return structured `permission_required` errors for network, destructive, or out-of-root operations instead of silently allowing them.
5. Borrow Gemini's checkpoint idea in a limited form: before `apply_patch`, compute affected files and either apply atomically or preserve enough preimage metadata for rollback/error reporting. Do not auto-commit like Aider in the shared repo.
6. Borrow Aider's repo-map idea only as P1/P2. The P0 server should stay primitive and deterministic; a future `symbol_map` or `repo_map` tool can be added after the core read/search/edit/test loop is stable.
7. Borrow mini-SWE-agent's output discipline: all command outputs need timeout, byte caps, return code, stderr/stdout separation, and clear truncation with head/tail snippets.
8. Use MCP Inspector CLI in `make test-mcp-contract` to verify initialize, `tools/list`, schema validity, and basic `tools/call` paths over the same transport users will use.
9. For dogfood, follow Claude/Gemini subagent scoping internally: give validation subagents only this MCP server's tools, record calls, and reject direct filesystem/shell bypass in the report.

## Designs To Borrow

- OpenCode: explicit tool inventory; `apply_patch` with relative paths embedded in patch markers; permission groups for `read`, `edit`, `bash`, `external_directory`; per-agent permission overrides.
- Claude Code: subagents with tool allowlists/denylists and scoped MCP servers; worktree isolation for parallel implementation experiments; hooks as a conceptual model for deterministic pre/post-tool checks; clear permission modes.
- Gemini CLI: root directory boundary, mutating-tool confirmations with diff previews, checkpoint snapshots, command restriction configuration, Docker/Podman/seatbelt sandbox options, MCP server include/exclude and trust flags.
- Aider: repo map for context efficiency, model-specific edit formats as evidence that edit APIs must be strict, `/diff` and `/undo` ergonomics, automatic test/lint feedback loops.
- SWE-agent: line/pagination-aware ACI, benchmark harness discipline, final patch submission, Docker-backed reproducibility.
- MCP Inspector/spec: schema-first contracts, structured tool output, annotations vocabulary, and scriptable Inspector CLI checks.

## Designs Unsuitable For This Project

- OpenCode's documented "all tools enabled by default" posture is too permissive for an MCP server intended to be reused by arbitrary clients.
- Claude's `bypassPermissions` and auto classifier are product-level behavior and should not be cloned. This project needs deterministic server-side policy, not an opaque model classifier.
- Gemini's model-assisted edit correction should not be part of `apply_patch`; it makes behavior nondeterministic and harder to test.
- Aider's auto-commit-on-edit behavior is unsafe in a multi-agent shared worktree. Use git status/diff and optional checkpoints instead.
- mini-SWE-agent's "single bash tool can do everything" interface is compact for benchmarks but too broad for a safe reusable MCP runtime.
- Browser/computer-use agents, web search/fetch, memory, skills/plugin marketplaces, login/account management, and model routing are outside this project's P0 scope.
- Exposing a public MCP `spawn_subagent` tool conflicts with the runtime-primitives goal and creates unclear ownership for permissions, worktrees, and output provenance.

## Risks

- Shell escape risk: any permission model based only on command strings can be bypassed through scripts, interpreters, redirection, compound commands, or package lifecycle hooks.
- Path escape risk: `../`, absolute paths, symlinks, hardlinks, generated temp files, and shell subprocesses can reach outside the workspace unless the server canonicalizes paths and the shell is sandboxed.
- Concurrent edits can race. `apply_patch` must define atomicity, conflict handling, and affected file reporting.
- MCP annotations are untrusted hints. They help clients display risk, but cannot replace server-side enforcement.
- Output growth can break clients or hide important failures. Every read/search/shell/diff path needs caps and truncation metadata.
- Dirty worktrees are common. The runtime must avoid auto-commits and should never revert user changes unless explicitly asked.
- Client approval support varies. `request_permissions` needs a structured fallback for clients without elicitation.
- Large reference repos and benchmark fixtures can pollute git history if `.reference/` and generated artifacts are not excluded.

## Action Items

1. Encode the P0 tool contract with explicit JSON schemas, output shapes, error codes, and MCP annotations.
2. Add compliance tests for root-relative path safety, symlink escape, binary reads, patch failures, command timeouts, output truncation, stdin sessions, and git diff/status.
3. Implement permission checks as server-side policy before tool execution; return `permission_required` rather than relying on the MCP client to infer risk.
4. Add Inspector CLI checks to compliance once the server exists.
5. Design dogfood subagents with tool allowlists that include only the MCP runtime tools and with logging that proves no direct shell/filesystem bypass occurred.
6. Treat sandboxing as required for trustworthy shell autonomy: P0 should block or request permission for risky shell/network operations; P1 should add OS/container isolation.
7. Keep repo-map/symbol intelligence, LSP operations, image/PDF reads, browser automation, and subagent orchestration out of P0 unless the core runtime loop is already stable and tested.
