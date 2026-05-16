# Codex Internals Research

## Task Scope

Research OpenAI Codex internals that are relevant to a coding-agent runtime MCP server. The target server is the lower-level runtime described in `CODEX_GOAL_MODE_MCP_RUNTIME_TASK.md`, not a wrapper around the Codex CLI or ChatGPT product features.

This report covers:

- Codex local tool capabilities.
- Which capabilities should be MCP-ified for this project.
- Which Codex capabilities should not be exposed.
- Tests and fixtures that can be reused or migrated.
- `apply_patch` semantics and limits.
- Shell, exec, session, and stdin semantics.
- Whether `view_image` is P1-worthy.

## Materials Read, Cloned, Referenced

- Project brief: `CODEX_GOAL_MODE_MCP_RUNTIME_TASK.md`.
- Local clone: `.reference/openai-codex`, shallow clone of `https://github.com/openai/codex`, reviewed at short commit `de9c5c0`. This directory is intentionally under `.reference/` and should not be committed.
- Codex CLI and MCP server:
  - `.reference/openai-codex/codex-rs/README.md`
  - `.reference/openai-codex/codex-rs/mcp-server/src/codex_tool_config.rs`
  - `.reference/openai-codex/codex-rs/mcp-server/src/message_processor.rs`
  - `.reference/openai-codex/codex-rs/mcp-server/src/lib.rs`
- `apply_patch` implementation and tests:
  - `.reference/openai-codex/codex-rs/apply-patch/src/parser.rs`
  - `.reference/openai-codex/codex-rs/apply-patch/src/lib.rs`
  - `.reference/openai-codex/codex-rs/apply-patch/apply_patch_tool_instructions.md`
  - `.reference/openai-codex/codex-rs/apply-patch/tests/suite/tool.rs`
  - `.reference/openai-codex/codex-rs/apply-patch/tests/suite/scenarios.rs`
  - `.reference/openai-codex/codex-rs/apply-patch/tests/fixtures/scenarios/`
- Shell, unified exec, sessions, and stdin:
  - `.reference/openai-codex/codex-rs/core/src/tools/handlers/shell_spec.rs`
  - `.reference/openai-codex/codex-rs/core/src/tools/handlers/shell.rs`
  - `.reference/openai-codex/codex-rs/core/src/tools/handlers/shell/shell_command.rs`
  - `.reference/openai-codex/codex-rs/core/src/tools/handlers/unified_exec.rs`
  - `.reference/openai-codex/codex-rs/core/src/tools/handlers/unified_exec/exec_command.rs`
  - `.reference/openai-codex/codex-rs/core/src/tools/handlers/unified_exec/write_stdin.rs`
  - `.reference/openai-codex/codex-rs/core/src/tools/runtimes/unified_exec.rs`
  - `.reference/openai-codex/codex-rs/core/src/unified_exec/mod.rs`
  - `.reference/openai-codex/codex-rs/core/src/unified_exec/process_manager.rs`
  - `.reference/openai-codex/codex-rs/core/src/tools/handlers/unified_exec_tests.rs`
  - `.reference/openai-codex/codex-rs/core/src/unified_exec/mod_tests.rs`
- Image viewing:
  - `.reference/openai-codex/codex-rs/core/src/tools/handlers/view_image.rs`
  - `.reference/openai-codex/codex-rs/core/src/tools/handlers/view_image_spec.rs`
  - `.reference/openai-codex/codex-rs/core/src/tools/image_detail_tests.rs`
  - `.reference/openai-codex/codex-rs/core/src/context_manager/history_tests.rs`
- Sandbox and approvals:
  - `.reference/openai-codex/codex-rs/protocol/src/protocol.rs`
  - `.reference/openai-codex/codex-rs/core/src/tools/sandboxing_tests.rs`
  - `.reference/openai-codex/docs/sandbox.md` was searched but the active docs are the public developer pages.
- Public OpenAI docs used as context:
  - `https://developers.openai.com/codex/mcp`
  - `https://developers.openai.com/codex/security`
  - `https://developers.openai.com/codex/config-reference`
  - `https://platform.openai.com/docs/guides/tools-apply-patch`
  - `https://developers.openai.com/api/docs/guides/tools-shell`

The operational details below come primarily from the public Codex repository because it contains the concrete schemas, handlers, and tests.

## Key Findings

### 1. Codex Local Tool Capabilities

Codex has local coding-agent primitives, but its own public MCP server is not that primitive surface.

The model-visible local capabilities in the reviewed source include:

- Command execution:
  - Legacy one-shot `shell_command`.
  - Unified `exec_command`.
  - `write_stdin` for live unified-exec sessions.
- File editing:
  - `apply_patch` as a freeform patch tool.
  - Shell interception for `apply_patch` command-shaped calls.
- Local image loading:
  - `view_image` for image files on disk, returning image content for the model.
- Permissions:
  - `request_permissions`, feature-gated by approval configuration.
- Planning and orchestration:
  - `update_plan`.
  - Goal tools.
  - Multi-agent tools such as `spawn_agent`, `send_input`, `wait_agent`, and `close_agent`.
- MCP client capability:
  - Codex can call tools exposed by configured MCP servers.

The reviewed Codex core does not primarily expose separate low-level file read/list/search tools. It relies heavily on shell commands such as `rg`, `sed`, `ls`, and `git` for read-only filesystem work. That is acceptable in a full CLI agent, but it is too broad for this project as a runtime MCP contract. This project should expose dedicated read-only file and search primitives so clients do not need shell access for basic inspection.

### 2. The Existing Codex MCP Server Is A High-Level Wrapper

`codex-rs/mcp-server` exposes two tools:

- `codex`: starts or continues a Codex agent task from a prompt.
- `codex-reply`: sends a follow-up prompt to an existing Codex thread.

The `codex` tool accepts product/runtime controls such as `prompt`, optional `model`, `profile`, `cwd`, `approval_policy`, `sandbox`, `config`, `base_instructions`, `developer_instructions`, and `compact_prompt`. Its output schema is a high-level `{ threadId, content }` shape. `tools/list` returns only `codex` and `codex-reply`; unknown tools return a tool-level error result.

This is useful as a reference for JSON-RPC stdio hygiene, but it is the wrong surface for this project. The project brief explicitly calls for runtime primitives, not a Codex-in-Codex wrapper.

Transport detail worth borrowing: the Codex MCP server uses stdin/stdout for JSON-RPC, keeps protocol output on stdout, and sends tracing/logging to stderr. That separation should be preserved if this project later adds stdio transport.

### 3. What Should Be MCP-ified

The project should MCP-ify the lower-level runtime operations from the brief:

- `read_file`, `list_dir`, `list_files`, and `search_text` as safe, workspace-bound read-only tools.
- `apply_patch` using Codex-style patch grammar, with project-specific workspace and symlink enforcement.
- `exec_command` and `write_stdin` using Codex unified-exec semantics as the baseline.
- `kill_session` as a project-specific addition. Codex has internal process termination and LRU pruning, but no model-visible `kill_session` tool in the reviewed local tool surface.
- `git_status` and `git_diff` as structured git primitives so clients do not need shell for routine review.
- `request_permissions` as a structured approval path, not as silent privilege escalation.
- `view_image` as P1, feature-gated.

### 4. What Should Not Be Exposed

Do not expose the following as runtime MCP tools:

- High-level Codex tools such as `codex`, `codex-reply`, or equivalent agent wrappers.
- ChatGPT or Codex account login, token, keyring, billing, or paid-routing features.
- Codex cloud tasks, remote queues, or cloud-environment management.
- Memory, personalization, user profile, or cross-session preference storage.
- Web search, arbitrary network fetch, browser automation, or image generation.
- Plugin marketplace, connector installation, or tool discovery/install flows.
- Model selection or OpenAI account routing controls.
- Subagent orchestration tools such as `spawn_agent` or `spawn_agents_on_csv`.
- Planning/goal tools such as `update_plan` and goal APIs as external runtime tools.
- Raw unrestricted shell or full Codex config override surfaces.
- Base/developer instruction injection through MCP.

Several of these are useful inside Codex as a product, but they would blur the runtime boundary and expand the security model beyond the project brief.

### 5. `apply_patch` Semantics And Limits

Codex `apply_patch` uses a custom envelope grammar. The relevant grammar in `parser.rs` is:

```text
start: begin_patch environment_id? hunk+ end_patch
begin_patch: "*** Begin Patch" LF
environment_id: "*** Environment ID: " filename LF
end_patch: "*** End Patch" LF?
hunk: add_hunk | delete_hunk | update_hunk
add_hunk: "*** Add File: " filename LF add_line+
delete_hunk: "*** Delete File: " filename LF
update_hunk: "*** Update File: " filename LF change_move? change?
filename: /(.+)/
add_line: "+" /(.+)/ LF -> line
change_move: "*** Move to: " filename LF
change: (change_context | change_line)+ eof_line?
change_context: ("@@" | "@@ " /(.+)/) LF
change_line: ("+" | "-" | " ") /(.+)/ LF
eof_line: "*** End of File" LF
```

Important behavior:

- It supports add, delete, update, and move/rename via `*** Move to:`.
- It supports an optional `*** Environment ID: ...` header for multi-environment Codex sessions. This project should omit that unless it later supports multiple workspaces.
- The parser is lenient in practice. It tolerates whitespace-padded markers and strips heredoc wrappers such as `<<EOF`, `<<'EOF'`, and `<<"EOF"` in command-shaped calls.
- The tool instructions tell the model to use relative file references only. The parser and tests accept both relative and absolute hunk paths, so this project must enforce workspace-relative or workspace-contained paths at the MCP layer.
- Add can overwrite an existing file and records the overwritten content in the delta.
- Delete fails on missing files and on directories; it is not recursive deletion.
- Update requires an existing file.
- Move writes the destination and then removes the source; it can overwrite the destination.
- Parent directories for added or moved files may be created as needed.
- Empty patches fail with "No files were modified."
- Application is not atomic across hunks. If an early hunk succeeds and a later hunk fails, the earlier file changes remain. Codex exposes failure with a delta; tests confirm partial success is left on disk.
- On write failure, delta exactness can become false because the filesystem may have changed before the error.
- Successful CLI output is a summary such as `Success. Updated the following files:` followed by `A`, `M`, and `D` entries.

Recommendation for this project: implement the Codex patch grammar for compatibility, but wrap it in a stricter server policy. Enforce workspace containment, reject symlink escapes, and choose one of two explicit semantics before P0 release:

- Prefer all-or-nothing apply with rollback on failure.
- If non-atomic behavior is retained, return structured partial-failure data including `ok: false`, `partial: true`, `affected_files`, and a clear delta/error summary.

The brief says "no half products", so silent partial application is not acceptable.

### 6. Shell, Exec, Session, And Stdin Semantics

Codex has two execution paths:

- Legacy `shell_command`:
  - One-shot command execution.
  - Parameters include `command`, `workdir`, `timeout_ms`, optional `login`, sandbox/approval fields, and permission fields.
  - No model-visible persistent session id or stdin path.
- Unified `exec_command`:
  - Parameters include `cmd`, optional `workdir`, `shell`, `login`, `tty`, `yield_time_ms`, `max_output_tokens`, sandbox/approval fields, and optional `environment_id`.
  - Description: "Runs a command in a PTY, returning output or a session ID for ongoing interaction."
  - Despite that description, `tty` defaults false. A PTY is only allocated when requested.
- `write_stdin`:
  - Parameters include `session_id`, optional `chars`, `yield_time_ms`, and `max_output_tokens`.
  - Empty `chars` means poll without writing.
  - Nonempty `chars` requires the original process to have been started with `tty: true`; otherwise stdin is closed.

Unified exec output schema includes:

- `chunk_id`
- `wall_time_seconds`
- `exit_code`
- `session_id`
- `original_token_count`
- `output`

Behavior worth carrying into this project:

- If a command exits within the initial yield window, the response includes `exit_code` and no `session_id`.
- If the command is still running after the yield window, the response includes `session_id`.
- A later `write_stdin` call returns more output and either a still-running `session_id` or a final `exit_code`.
- An empty `write_stdin` call is a poll.
- Once a process exits and is removed, subsequent writes return unknown-process errors.
- `yield_time_ms` is clamped. Codex constants include minimum 250 ms, empty-poll minimum 5000 ms, maximum 30000 ms for ordinary yields, and a default background terminal timeout of 300000 ms.
- Default max output is 10000 tokens, with a hard unified-exec output byte cap of 1 MiB.
- Codex limits unified exec processes to 64 and prunes older background processes, protecting the most recent ones.
- Workdir is resolved against the active environment cwd.
- Login shell usage can be disabled. If disabled, `login: true` is rejected.
- Production session ids are randomized in a broad numeric range; tests use deterministic ids.
- Output is buffered with truncation behavior tested by head-tail buffer tests.

Project-specific recommendation: use the unified-exec model, not the legacy one-shot model, but add `kill_session` as an explicit tool. Keep `cmd` for Codex compatibility or accept both `cmd` and `command` with one canonical output shape. Require `tty: true` for interactive stdin. Default to non-TTY execution for ordinary commands.

### 7. Sandbox And Approval Notes

Codex protocol has approval policies such as `untrusted`, deprecated `on-failure`, `on-request`, `granular`, and `never`. Sandbox policies include `danger-full-access`, `read-only`, `workspace-write`, and external sandbox modes. Workspace-write policy has details for writable roots and protected metadata paths.

This project should not clone the entire Codex product sandbox stack for P0. It should implement a smaller, enforceable runtime policy:

- One canonical workspace root.
- Shared path resolver for every filesystem, git, patch, image, and cwd input.
- Absolute paths rejected by default, or accepted only after canonical workspace containment.
- No symlink escape.
- No writes outside the workspace.
- Network denied by default.
- Explicit approval flow for higher-risk exec cases.
- Output, timeout, process count, and session idle limits.

The Codex approval/sandbox source is still useful as a vocabulary and as a reminder that permissions must be field-driven, not inferred from command strings alone.

### 8. Tests That Can Be Reused Or Migrated

Best test sources to migrate or adapt:

- `codex-rs/apply-patch/tests/fixtures/scenarios/`
  - Golden scenarios for add, update, delete, multi-op patches, multi-chunk patches, move to new directory, overwrite behavior, Unicode, EOF markers, whitespace-padded markers, missing context, missing files, delete-directory failure, trailing newline handling, and partial success.
- `codex-rs/apply-patch/tests/suite/tool.rs`
  - CLI-style success/error output and partial failure behavior.
- `codex-rs/apply-patch/src/parser.rs` tests
  - Parser grammar, lenient heredoc handling, hunk path parsing, and absolute-path acceptance. For this project, keep parser acceptance tests but add MCP policy tests that reject absolute paths escaping the workspace.
- `codex-rs/core/src/tools/handlers/apply_patch_tests.rs`
  - Handler-level verification, environment-id behavior, streamed diff consumption, hook payload shaping, and apply-patch shell interception.
- `codex-rs/core/src/tools/handlers/unified_exec_tests.rs`
  - Command resolution, explicit shell behavior, login rejection, hook payloads, and `write_stdin` preserving original exec call identity.
- `codex-rs/core/src/unified_exec/mod_tests.rs`
  - Session persistence, multiple session isolation, timeout then poll retrieval, head-tail buffering, pause extending yield, and remote/local process contracts.
- `codex-rs/protocol/src/exec_output_tests.rs`
  - Exec output encoding/decoding behavior.
- `codex-rs/core/src/tools/image_detail_tests.rs`
  - Original image detail support and sanitization.
- `codex-rs/core/src/context_manager/history_tests.rs`
  - Image payload sizing and capping behavior.
- `codex-rs/core/src/tools/sandboxing_tests.rs`
  - Workspace-write and sandbox-policy expectations.

Migration guidance:

- Do not copy OpenAI tests verbatim without checking license and attribution requirements.
- Port scenario ideas and expected behavior into this repo's own fixtures.
- Add project-specific tests for MCP schemas, workspace confinement, symlink escape rejection, permission denials, structured failure shapes, and JSON-RPC error boundaries.

### 9. Is `view_image` P1-Worthy?

Yes. `view_image` is P1-worthy, but not P0.

Reasons to include it in P1:

- Frontend and UI coding agents need to inspect screenshots, generated assets, visual regressions, and design references.
- Codex already treats local image viewing as a useful model-facing primitive.
- The implementation boundary is manageable: it reads a local file, validates image bytes, and returns image content with a detail hint.

Reasons not to make it P0:

- Core coding workflows can be handled with text file tools, patching, exec, git status/diff, and tests.
- Image handling needs separate file size, MIME, decode, dimension, and prompt payload limits.
- It increases the blast radius of path handling if implemented before the shared workspace resolver is hardened.

P1 requirements:

- Workspace-contained paths only.
- File must be a regular image file.
- MIME/type detection from bytes, not only extension.
- File size and pixel dimension limits.
- Optional `detail` support only if the client/model path can consume it.
- Return MCP image content or a structured data URL, matching the profile contract.

## Concrete Recommendations For This Project

1. Implement the P0 surface as runtime primitives, not as a Codex wrapper:
   - `read_file`
   - `list_dir`
   - `list_files`
   - `search_text`
   - `apply_patch`
   - `exec_command`
   - `write_stdin`
   - `kill_session`
   - `git_status`
   - `git_diff`
   - `request_permissions`

2. Treat Codex `exec_command` and `write_stdin` as the baseline behavior:
   - `cmd` string.
   - Optional `workdir`.
   - Optional `shell`.
   - `login` boolean.
   - `tty` boolean, default false.
   - `yield_time_ms`.
   - `max_output_tokens`.
   - Structured result with output, session id, exit code, timing, and truncation metadata.

3. Add `kill_session` explicitly:
   - Kill process group, not just the parent process.
   - Return whether the session existed, whether it exited, signal/exit data when available, and any final output.
   - Test idempotent unknown-session failure separately from successful kill.

4. Use Codex `apply_patch` grammar, but tighten policy:
   - No absolute path escape.
   - No symlink escape.
   - No writes outside workspace.
   - Clear atomic or partial semantics.
   - Structured result listing changed files and operations.

5. Make basic file and git reads first-class:
   - This is safer than forcing clients through shell.
   - It also makes MCP schemas and permissions easier to validate.

6. Keep high-level product features out:
   - Do not expose `codex`, `codex-reply`, model selection, cloud tasks, subagents, memory, web search, or connector install flows.

7. Reuse test intent aggressively:
   - Start with migrated apply-patch scenario fixtures.
   - Add unified-exec session tests before exposing interactive commands.
   - Add MCP contract tests around every structured failure.

8. Put `view_image` behind a P1 feature flag:
   - Implement only after the shared path resolver and output limits are in place.

## Risks

- `apply_patch` parser compatibility can accidentally allow paths the model instructions say not to use. The server must enforce path policy after parsing.
- Non-atomic patch application can leave partial edits after failure. That is dangerous for automated MCP clients unless the response makes the partial state unmistakable or the implementation rolls back.
- Shell execution is inherently broad. Dedicated file/git tools reduce the need for shell but do not remove the need for command sandboxing.
- Interactive sessions can outlive the request that created them. They need idle cleanup, process-tree termination, ownership checks, and bounded output.
- PTY behavior differs across platforms. Tests need to cover both non-TTY command execution and PTY-backed stdin workflows.
- Output truncation can hide important failure lines. Return truncation metadata and prefer head-tail retention for long-running commands.
- `view_image` can become an unintended file exfiltration path if path handling is weaker than the text file tools.
- Copying the high-level Codex MCP server shape would violate the project boundary and create a much larger product/security surface.

## Action Items

1. Create project-native fixture tests from Codex apply-patch scenarios, including partial failure and absolute-path policy rejection.
2. Define the final `apply_patch` transaction semantics before implementation: rollback or explicit partial result.
3. Implement one shared workspace path resolver before any file, patch, image, git, or exec cwd tool.
4. Specify and test unified-exec result schemas, including session lifecycle, stdin polling, output truncation, and unknown session errors.
5. Add `kill_session` contract tests because Codex does not expose it as a direct model tool.
6. Implement read-only file and git primitives before broad shell execution.
7. Add permission tests for network, destructive commands, TTY sessions, login shells, and cwd changes.
8. Keep `view_image` as P1 until P0 path and output limits are proven.
9. Keep `.reference/openai-codex` uncommitted; use it only as a local reference source.
