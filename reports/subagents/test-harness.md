# Test Harness Subagent Report

## Task Scope

- Role: `test-harness-engineer`.
- Built tests before runtime implementation.
- Owned changes under `tests/`, `Makefile` compliance targets, generated compliance report skeleton/output under `reports/compliance/`, and this report.
- Did not implement server runtime logic under `src/`.

## Materials Read

- `CODEX_GOAL_MODE_MCP_RUNTIME_TASK.md`, especially sections 6-10 for P0 tool contract, fixtures, golden cases, security cases, E2E, Codex compatibility, and dogfood requirements.
- Local reference checkout under `.reference/openai-codex/`, with targeted searches around `apply_patch`, unified exec, MCP, truncation, and view image tests.

## Artifacts Produced

- `Makefile`
  - `make compliance`
  - `make test-mcp-contract`
  - `make test-tool-golden`
  - `make test-security`
  - `make test-e2e`
  - `make test-codex-compat`
  - `make dogfood-mcp`
  - `make report`
- `tests/compliance/runner.py`
  - stdlib-only unittest runner.
  - Writes `reports/compliance/latest.json` and `reports/compliance/latest.md`.
- `tests/compliance/mcp_client.py`
  - Streamable HTTP JSON-RPC MCP client.
  - Starts `codex-tool-runtime-mcp --workspace <fixture> --host 127.0.0.1 --port <port>` by default.
  - Supports `CODEX_TOOL_RUNTIME_SERVER_CMD` and `CODEX_TOOL_RUNTIME_SERVER_URL`.
- `tests/compliance/fixtures/`
  - `tiny-js-project`
  - `tiny-python-project`
  - `long-running-project`
  - `image-project`
  - `malicious-project`
- `tests/compliance/outside-secret.txt`
- `tests/compliance/codex_compat/semantic_vectors.json`
- Test modules:
  - `test_mcp_contract.py`
  - `test_tool_golden.py`
  - `test_security.py`
  - `test_e2e.py`
  - `test_codex_compat.py`
  - `test_dogfood.py`

## Key Coverage

- MCP contract:
  - `initialize`
  - `tools/list`
  - required P0 tools
  - forbidden product-layer tools
  - input schema sanity
  - structured success and failure shapes
  - unknown tool behavior
  - stdout pollution guard
- Golden tools:
  - `read_file`, `list_dir`, `list_files`, `search_text`
  - `apply_patch` add/update/delete/move/failure/path safety
  - `exec_command`, `write_stdin`, `kill_session`
  - `git_status`, `git_diff`
- Security:
  - traversal, absolute path, symlink escape
  - command workdir escape and shell attempts to read outside workspace
  - destructive command guardrails
  - network default policy
  - sensitive env stripping
  - concurrent read-only calls
- Deterministic E2E:
  - JS bugfix loop
  - Python function-add loop
  - long-running stdin loop
  - workspace escape loop
  - optional P1 `view_image`
- Codex compatibility:
  - Codex-style apply_patch envelope semantic vectors
  - exec/session/stdin behavior vectors
  - optional image behavior when exposed
- Dogfood skeleton:
  - deterministic MCP-only agent loop that records MCP tool calls and avoids direct filesystem/shell bypass.

## Expected Current Failures

`make compliance` currently fails before runtime assertions because no MCP runtime executable exists yet:

```text
MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL.
Default command: codex-tool-runtime-mcp --workspace <fixture> --host 127.0.0.1 --port <port>
```

Current generated report:

- `reports/compliance/latest.json`
- `reports/compliance/latest.md`

Current result:

- tests run: 29
- passed: false
- failures: 29
- expected reason: missing server runtime command/URL, not runtime semantic failures yet.

## Implementation Handoff

- Implement the P0 streamable HTTP MCP server and expose `codex-tool-runtime-mcp`.
- Keep logs on stderr. The tests assert stdout remains clean.
- Match these tool argument names:
  - `read_file`: `path`, `start_line`, `end_line`, `max_bytes`
  - `list_dir`: `path`, `include_hidden`, `max_results`
  - `list_files`: `glob`, `path`, `max_results`
  - `search_text`: `query`, `path`, `glob`, `context_lines`, `max_results`
  - `apply_patch`: `patch`
  - `exec_command`: `cmd`, `workdir`, `timeout_ms`, `max_output_bytes`, `tty`
  - `write_stdin`: `session_id`, `chars`
  - `kill_session`: `session_id`
  - `git_diff`: `path`, `max_bytes`
- Return MCP tool results with `content` and preferably `structuredContent`.
- For tool-level denials, either return MCP `isError=true` with structured content or a JSON-RPC error with `code` and `message`.

## Risks

- The security tests intentionally require more than path normalization; `exec_command` must prevent command-level outside-workspace reads, not only invalid `workdir`.
- Network-denial behavior must be deterministic, otherwise the suite can become environment-dependent.
- The Python fixture uses a local `pytest.py` shim so the compliance suite does not depend on installing external pytest.
- P1 `view_image` tests are skipped only when the tool is absent; if the tool is exposed, it must pass.

## Action Items

- Implementation engineer: implement server runtime until `make compliance` reaches semantic failures, then iterate against the failing cases.
- Security engineer: review command-denial expectations before runtime ships.
- Benchmark/dogfood engineer: reuse `test_dogfood.py` as the deterministic MCP-only path and extend it for benchmark reporting.
