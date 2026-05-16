# Compliance Report

- profile: `codex-tool-runtime-mcp-v0.1`
- commit: `4f36b400c1a653efdff2a39d5a635722d83c2fbf`
- suite: `all`
- passed: `false`
- tests_run: `29`
- elapsed_seconds: `0.644`

## Required Tools

- `read_file`: failed
- `list_dir`: failed
- `list_files`: failed
- `search_text`: failed
- `apply_patch`: failed
- `exec_command`: failed
- `write_stdin`: failed
- `kill_session`: failed
- `git_status`: failed
- `git_diff`: failed
- `request_permissions`: failed

## Failures

### tests.compliance.test_mcp_contract.MCPContractTests.test_each_tool_has_valid_basic_json_schema

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-7g8c6ns9/tiny-js-project --host 127.0.0.1 --port 44827`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-7g8c6ns9/tiny-js-project --host 127.0.0.1 --port 44827

```

### tests.compliance.test_mcp_contract.MCPContractTests.test_initialize_succeeds_and_tools_list_is_available

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-126h61dm/tiny-js-project --host 127.0.0.1 --port 51961`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-126h61dm/tiny-js-project --host 127.0.0.1 --port 51961

```

### tests.compliance.test_mcp_contract.MCPContractTests.test_server_does_not_write_debug_logs_to_stdout

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-z50dwx6i/tiny-js-project --host 127.0.0.1 --port 52767`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-z50dwx6i/tiny-js-project --host 127.0.0.1 --port 52767

```

### tests.compliance.test_mcp_contract.MCPContractTests.test_success_and_failure_paths_return_structured_tool_results

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-b9upvme5/tiny-js-project --host 127.0.0.1 --port 52513`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-b9upvme5/tiny-js-project --host 127.0.0.1 --port 52513

```

### tests.compliance.test_mcp_contract.MCPContractTests.test_tools_list_contains_all_required_p0_tools

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-xb4d71y2/tiny-js-project --host 127.0.0.1 --port 53027`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-xb4d71y2/tiny-js-project --host 127.0.0.1 --port 53027

```

### tests.compliance.test_mcp_contract.MCPContractTests.test_tools_list_excludes_forbidden_product_layer_tools

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-sys5evwv/tiny-js-project --host 127.0.0.1 --port 56699`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-sys5evwv/tiny-js-project --host 127.0.0.1 --port 56699

```

### tests.compliance.test_mcp_contract.MCPContractTests.test_unknown_tool_returns_standard_json_rpc_error_or_tool_error

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-6oegrifg/tiny-js-project --host 127.0.0.1 --port 36707`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-6oegrifg/tiny-js-project --host 127.0.0.1 --port 36707

```

### tests.compliance.test_tool_golden.ApplyPatchGoldenTests.test_apply_patch_add_update_delete_move_and_context_mismatch

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-zbii91qn/tiny-js-project --host 127.0.0.1 --port 42527`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-zbii91qn/tiny-js-project --host 127.0.0.1 --port 42527

```

### tests.compliance.test_tool_golden.ApplyPatchGoldenTests.test_apply_patch_rejects_absolute_traversal_and_symlink_escape

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-hleqk_s8/tiny-js-project --host 127.0.0.1 --port 57167`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-hleqk_s8/tiny-js-project --host 127.0.0.1 --port 57167

```

### tests.compliance.test_tool_golden.ExecAndGitGoldenTests.test_exec_command_success_nonzero_timeout_output_cap_and_permissions

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-rbxbn3j4/tiny-js-project --host 127.0.0.1 --port 46051`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-rbxbn3j4/tiny-js-project --host 127.0.0.1 --port 46051

```

### tests.compliance.test_tool_golden.ExecAndGitGoldenTests.test_write_stdin_kill_session_git_status_and_git_diff

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-joi6o_3o/tiny-js-project --host 127.0.0.1 --port 53611`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-joi6o_3o/tiny-js-project --host 127.0.0.1 --port 53611

```

### tests.compliance.test_tool_golden.ListAndSearchGoldenTests.test_list_dir_and_list_files_exclude_defaults_and_truncate

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-eggh98xi/tiny-js-project --host 127.0.0.1 --port 48529`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-eggh98xi/tiny-js-project --host 127.0.0.1 --port 48529

```

### tests.compliance.test_tool_golden.ListAndSearchGoldenTests.test_search_text_query_glob_context_and_max_results

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-qh7ad66j/tiny-js-project --host 127.0.0.1 --port 51853`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-qh7ad66j/tiny-js-project --host 127.0.0.1 --port 51853

```

### tests.compliance.test_tool_golden.ReadFileGoldenTests.test_read_file_normal_line_range_truncation_binary_and_escape

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-racpi4dl/tiny-js-project --host 127.0.0.1 --port 58643`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-racpi4dl/tiny-js-project --host 127.0.0.1 --port 58643

```

### tests.compliance.test_security.SecurityComplianceTests.test_concurrent_read_only_tool_calls_are_stable

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-malicious-project-dar1f0z5/malicious-project --host 127.0.0.1 --port 46129`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-malicious-project-dar1f0z5/malicious-project --host 127.0.0.1 --port 46129

```

### tests.compliance.test_security.SecurityComplianceTests.test_exec_workdir_shell_escape_destructive_and_network_are_rejected

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-malicious-project-a7ntrknl/malicious-project --host 127.0.0.1 --port 33683`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-malicious-project-a7ntrknl/malicious-project --host 127.0.0.1 --port 33683

```

### tests.compliance.test_security.SecurityComplianceTests.test_path_traversal_absolute_paths_and_symlink_escape_are_rejected

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-malicious-project-ke6cvgn_/malicious-project --host 127.0.0.1 --port 35919`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-malicious-project-ke6cvgn_/malicious-project --host 127.0.0.1 --port 35919

```

### tests.compliance.test_security.SecurityComplianceTests.test_sensitive_environment_is_not_leaked_to_child_processes

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-malicious-project-07tbsr64/malicious-project --host 127.0.0.1 --port 50251`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-malicious-project-07tbsr64/malicious-project --host 127.0.0.1 --port 50251

```

### tests.compliance.test_security.SecurityComplianceTests.test_stdout_json_rpc_pollution_is_absent

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-malicious-project-ikpyccmr/malicious-project --host 127.0.0.1 --port 45093`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-malicious-project-ikpyccmr/malicious-project --host 127.0.0.1 --port 45093

```

### tests.compliance.test_e2e.DeterministicE2ETests.test_js_bugfix_search_patch_test_and_diff

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-dmjeo5b4/tiny-js-project --host 127.0.0.1 --port 33379`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-dmjeo5b4/tiny-js-project --host 127.0.0.1 --port 33379

```

### tests.compliance.test_e2e.DeterministicE2ETests.test_long_running_stdin_session

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-_wagj7a8/tiny-js-project --host 127.0.0.1 --port 53683`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-_wagj7a8/tiny-js-project --host 127.0.0.1 --port 53683

```

### tests.compliance.test_e2e.DeterministicE2ETests.test_python_add_function_patch_test_and_diff

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-1cm5n_ih/tiny-js-project --host 127.0.0.1 --port 37569`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-1cm5n_ih/tiny-js-project --host 127.0.0.1 --port 37569

```

### tests.compliance.test_e2e.DeterministicE2ETests.test_view_image_optional_p1_contract_when_exposed

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-_1zi8ph4/tiny-js-project --host 127.0.0.1 --port 44161`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-_1zi8ph4/tiny-js-project --host 127.0.0.1 --port 44161

```

### tests.compliance.test_e2e.DeterministicE2ETests.test_workspace_escape_flow_is_denied

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-367y3pdq/tiny-js-project --host 127.0.0.1 --port 46899`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-367y3pdq/tiny-js-project --host 127.0.0.1 --port 46899

```

### tests.compliance.test_codex_compat.CodexCompatibilityTests.test_apply_patch_envelope_semantic_vectors

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-dcfpcci6/tiny-js-project --host 127.0.0.1 --port 56987`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-dcfpcci6/tiny-js-project --host 127.0.0.1 --port 56987

```

### tests.compliance.test_codex_compat.CodexCompatibilityTests.test_missing_and_closed_sessions_return_structured_errors

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-n3fxwyzp/tiny-js-project --host 127.0.0.1 --port 45445`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-n3fxwyzp/tiny-js-project --host 127.0.0.1 --port 45445

```

### tests.compliance.test_codex_compat.CodexCompatibilityTests.test_session_semantics_match_codex_style_exec_and_stdin

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-b9pe4pcq/tiny-js-project --host 127.0.0.1 --port 55141`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-b9pe4pcq/tiny-js-project --host 127.0.0.1 --port 55141

```

### tests.compliance.test_codex_compat.CodexCompatibilityTests.test_view_image_semantics_when_p1_tool_is_present

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-kui_cw70/tiny-js-project --host 127.0.0.1 --port 41979`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-kui_cw70/tiny-js-project --host 127.0.0.1 --port 41979

```

### tests.compliance.test_dogfood.DogfoodMCPOnlyTests.test_mcp_only_agent_completes_js_bugfix_without_direct_bypass

- kind: `failure`
- message: `MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-qn0xhb5a/tiny-js-project --host 127.0.0.1 --port 59963`

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/local/lib/python3.11/unittest/case.py", line 619, in run
    self._callSetUp()
  File "/usr/local/lib/python3.11/unittest/case.py", line 576, in _callSetUp
    self.setUp()
  File "/root/codex-tool-mcp/tests/compliance/test_support.py", line 20, in setUp
    self.client = self.client_cm.__enter__()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/codex-tool-mcp/tests/compliance/mcp_client.py", line 106, in __enter__
    raise MCPTransportError(
tests.compliance.mcp_client.MCPTransportError: MCP server command is unavailable. Set CODEX_TOOL_RUNTIME_SERVER_CMD or CODEX_TOOL_RUNTIME_SERVER_URL. Default command: codex-tool-runtime-mcp --workspace /tmp/codex-mcp-tiny-js-project-qn0xhb5a/tiny-js-project --host 127.0.0.1 --port 59963

```

