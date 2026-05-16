# MCP Contract Architect Report

## Task Scope

Define the MCP tool surface, input schemas, output schemas, error model, annotations/hints, transport expectations, protocol behavior, and forbidden product-layer capabilities for a coding-agent runtime MCP server.

Required output:

- `reports/subagents/mcp-contract.md`
- `docs/profile-v0.1.md`

Implementation files were intentionally not created.

## References Consulted

- Project task brief: `CODEX_GOAL_MODE_MCP_RUNTIME_TASK.md`
- MCP tools specification: https://modelcontextprotocol.io/specification/2025-06-18/server/tools
- MCP lifecycle: https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle
- MCP transports: https://modelcontextprotocol.io/specification/2025-06-18/basic/transports
- MCP schema reference: https://modelcontextprotocol.io/specification/2025-06-18/schema
- MCP elicitation: https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation

The official MCP 2025-06-18 pages establish that tools are model-controlled capabilities with `inputSchema`, optional `outputSchema`, optional annotations, and `tools/list`/`tools/call` JSON-RPC methods. They also define lifecycle initialization, Streamable HTTP, stdio constraints, image content, structured content, and elicitation for user-mediated approval.

## Contract Decision Summary

The authoritative profile is in `docs/profile-v0.1.md`.

Key decisions:

- Target protocol is MCP `2025-06-18`.
- P0 transport is Streamable HTTP; P1 transport is stdio.
- All P0 tools are included: `read_file`, `list_dir`, `list_files`, `search_text`, `apply_patch`, `exec_command`, `write_stdin`, `kill_session`, `git_status`, `git_diff`, and `request_permissions`.
- `view_image` is P1 and may be feature-gated.
- Every tool returns MCP `content` plus `structuredContent`; the text content mirrors structured JSON for compatibility.
- Every tool has an `outputSchema`, even though MCP marks it optional, because compliance tests need stable structured results.
- Tool execution failures use `isError: true` with `structuredContent.ok: false`.
- Unknown tools and malformed arguments use JSON-RPC errors instead of tool-level errors.
- Workspace escape is never grantable in v0.1.
- Permission grants can use MCP elicitation when the client supports it; otherwise unsupported approval returns structured failure unless the server was explicitly started in a documented non-default permission mode.
- The profile forbids high-level Codex/product-layer wrappers and unrelated personal/account/network/model tools.

## Tool Surface

P0 tools:

| Tool | Purpose | Annotation posture |
| --- | --- | --- |
| `read_file` | Read a text slice inside the workspace | read-only, idempotent, closed-world |
| `list_dir` | List directory entries | read-only, idempotent, closed-world |
| `list_files` | List files by glob/ignore rules | read-only, idempotent, closed-world |
| `search_text` | Search text with bounded results | read-only, idempotent, closed-world |
| `apply_patch` | Apply Codex-style patch envelope | write-capable, destructive, non-idempotent |
| `exec_command` | Run bounded commands in the workspace | write-capable, destructive, non-idempotent, open-world when permissions allow network |
| `write_stdin` | Send input to a managed exec session | write-capable, non-idempotent |
| `kill_session` | Terminate a managed exec session | write-capable, destructive |
| `git_status` | Report git working tree status | read-only, idempotent |
| `git_diff` | Report unified git diff | read-only, idempotent |
| `request_permissions` | Request scoped approval for dangerous operations | workspace-read-only, non-idempotent approval flow |

P1 tool:

| Tool | Purpose | Annotation posture |
| --- | --- | --- |
| `view_image` | Return workspace image content | read-only, idempotent, closed-world |

Forbidden tools and aliases:

- memory, personalization, or profile storage
- ChatGPT/Codex login, account, token, or keyring management
- Codex cloud tasks or remote queues
- web search or arbitrary network fetch as a direct tool
- image generation
- subagent spawning or orchestration
- model selection or paid account routing
- plugin marketplace or connector installation
- high-level `codex(prompt)`, `codex-reply`, or equivalent agent wrappers

## Protocol Behavior

### initialize

The server must respond with protocol version `2025-06-18`, `capabilities.tools`, `serverInfo`, and short runtime instructions. It must not advertise prompts, resources, sampling, or product capabilities unless future profile versions define and test them.

The profile sets `tools.listChanged` to `false` because the tool list is fixed for a server process. A future feature-gated implementation may set it to `true` only if it sends `notifications/tools/list_changed` when the set changes.

### tools/list

`tools/list` returns all P0 tools. `view_image` appears only when P1 image support is enabled. Results may be unpaginated because the list is small; if pagination is implemented, cursors must be opaque and invalid cursors return JSON-RPC `-32602`.

Each tool entry must include:

- `name`
- `title`
- `description`
- `inputSchema`
- `outputSchema`
- `annotations`

### tools/call

The server validates:

1. The JSON-RPC request shape.
2. Tool name.
3. Arguments against the tool `inputSchema`.
4. Workspace/path/session/permission policy.

Valid calls return MCP tool results. Success has `isError: false`; execution failure has `isError: true`. Both include `structuredContent`.

Unknown tool names return JSON-RPC `-32602` with `error.data.reason = "unknown_tool"`. Invalid arguments return `-32602`. Unexpected pre-result failures return `-32603`.

## Input and Output Schemas

The full schema contract is in `docs/profile-v0.1.md`.

Schema highlights:

- Path parameters are workspace-relative strings.
- Absolute paths are rejected by default.
- `read_file` supports `start_line`, `end_line`, `max_bytes`, and UTF-8 text only.
- `list_dir` and `list_files` expose bounded `max_entries`/`max_results` controls and ignore large/generated directories by default.
- `search_text` supports literal or regex search, glob filters, bounded context, and truncation.
- `apply_patch` accepts only the Codex-style `*** Begin Patch` / `*** End Patch` envelope and supports add, update, delete, and move.
- `exec_command` requires bounded timeout/output controls and returns either final process output or a server-managed `session_id`.
- `write_stdin` and `kill_session` operate only on sessions created by this server.
- `git_status` and `git_diff` expose structured git metadata with bounded output.
- `request_permissions` returns a grant, denial, unsupported status, or structured error.
- `view_image` returns MCP image content or a data URL, subject to image type and size limits.

## Error Model

The contract separates protocol errors from tool execution errors.

Protocol errors:

- `-32601`: unknown JSON-RPC method
- `-32602`: invalid request params, invalid schema, invalid cursor, or unknown tool name inside `tools/call`
- `-32603`: unexpected internal failure before the server can construct a tool result

Tool execution errors:

- Returned as `tools/call` results with `isError: true`
- `structuredContent.ok` is `false`
- `structuredContent.error` includes `code`, `message`, `category`, `retryable`, optional `details`, and optional `permission_request`

Primary tool error codes:

- `INVALID_ARGUMENT`
- `PATH_OUTSIDE_WORKSPACE`
- `ABSOLUTE_PATH_DENIED`
- `SYMLINK_ESCAPE`
- `NOT_FOUND`
- `NOT_A_DIRECTORY`
- `IS_DIRECTORY`
- `BINARY_FILE`
- `UNSUPPORTED_ENCODING`
- `OUTPUT_TOO_LARGE`
- `TIMEOUT`
- `SESSION_NOT_FOUND`
- `SESSION_CLOSED`
- `COMMAND_REJECTED`
- `PERMISSION_REQUIRED`
- `PERMISSION_DENIED`
- `ELICITATION_UNSUPPORTED`
- `PATCH_FAILED`
- `GIT_ERROR`
- `INTERNAL_ERROR`

## Security and Permission Contract

The server binds one workspace root at startup. All path-bearing tools canonicalize candidate paths and verify the result remains inside that root. Symlink escapes are rejected. Listing may show a symlink but must not follow it outside the workspace.

`exec_command` must run in a workspace-contained working directory with timeouts and output caps. It must deny or permission-gate network use, destructive commands, broad permission changes, sensitive environment access, and long timeouts.

`request_permissions` is the only P0 approval tool. If a client advertises MCP elicitation, the server may use `elicitation/create` to ask for user approval. If not, it returns `ELICITATION_UNSUPPORTED` unless the process was explicitly started in a non-default permissive mode for disposable environments. The default must not silently open dangerous permissions.

Workspace escape is not grantable. This keeps path safety independent from the permission model.

## Transport Expectations

Streamable HTTP is required for P0:

- single endpoint, default `/mcp`
- POST for client messages
- optional GET SSE stream or `405`
- `MCP-Protocol-Version` after initialization
- optional `Mcp-Session-Id`
- Origin validation
- loopback bind by default
- no debug output outside JSON-RPC/SSE frames

stdio is P1:

- newline-delimited JSON-RPC over stdin/stdout
- stdout contains only MCP messages
- stderr is for logs

## Compliance Hooks

Contract tests should assert:

- `initialize` succeeds.
- `tools/list` includes every P0 tool.
- `tools/list` excludes forbidden product-layer tools.
- Each listed tool has valid JSON Schema for `inputSchema` and `outputSchema`.
- Tool annotations match the profile.
- `tools/call` success returns `content`, `structuredContent`, and `isError: false`.
- Tool execution errors return `isError: true` with structured error content.
- Unknown tool names return JSON-RPC error.
- stdout/HTTP response bodies are not polluted by logs.
- Path traversal, absolute paths, symlink escape, unsafe commands, session abuse, and network-by-default cases fail or require permission.

## Risks

- MCP `ToolAnnotations` are hints, not a security boundary. The server must enforce policy independently.
- Static annotations cannot perfectly describe `exec_command`; the contract marks it destructive and open-world because permissions may allow network or side effects.
- Elicitation support is client-dependent. The fallback path must be tested so permission-required cases are explicit rather than silently allowed.
- Atomic patch application is a hard requirement. If direct application cannot be guaranteed atomic, the implementation should stage changes and swap them into place only after validation.
- Shell command safety cannot rely on deny lists alone. The P0 contract defines guardrails; stronger OS sandboxing should be covered by the security architect.

## Follow-up Action Items

- Implementation engineer: generate tool definitions directly from the profile or a single source of truth to avoid schema drift.
- Test harness engineer: convert every schema and error case in `docs/profile-v0.1.md` into contract tests.
- Security architect: refine command sandbox and environment filtering details without weakening this contract.
- Release docs engineer: reference `docs/profile-v0.1.md` from README, SPEC, SECURITY, and COMPLIANCE once those documents exist.
