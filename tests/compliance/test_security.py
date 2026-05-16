from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

from tests.compliance.mcp_client import MCPClient
from tests.compliance.test_support import ComplianceTestCase


class SecurityComplianceTests(ComplianceTestCase):
    fixture_name = "malicious-project"

    def test_path_traversal_absolute_paths_and_symlink_escape_are_rejected(self) -> None:
        self.assert_denied_or_permission_required("read_file", {"path": "../outside-secret.txt"})
        self.assert_denied_or_permission_required("read_file", {"path": str(self.workspace.outside_secret)})
        self.assert_denied_or_permission_required("read_file", {"path": "outside-link.txt"})

        absolute_patch = f"""*** Begin Patch
*** Add File: {self.workspace.outside_secret}
+unsafe
*** End Patch
"""
        self.assert_denied_or_permission_required("apply_patch", {"patch": absolute_patch})

        traversal_patch = """*** Begin Patch
*** Update File: ../outside-secret.txt
@@
-TOP_SECRET_DO_NOT_READ
+unsafe
*** End Patch
"""
        self.assert_denied_or_permission_required("apply_patch", {"patch": traversal_patch})

        symlink_patch = """*** Begin Patch
*** Update File: outside-link.txt
@@
-TOP_SECRET_DO_NOT_READ
+unsafe
*** End Patch
"""
        self.assert_denied_or_permission_required("apply_patch", {"patch": symlink_patch})

    def test_exec_workdir_shell_escape_destructive_and_network_are_rejected(self) -> None:
        self.assert_denied_or_permission_required("exec_command", {"cmd": "pwd", "workdir": ".."})
        self.assert_denied_or_permission_required("exec_command", {"cmd": "cat ../outside-secret.txt"})
        self.assert_denied_or_permission_required("exec_command", {"cmd": "cat outside-link.txt"})
        self.assert_denied_or_permission_required("exec_command", {"cmd": "rm -rf /"})
        self.assert_denied_or_permission_required("exec_command", {"cmd": "git reset --hard"})
        self.assert_denied_or_permission_required("exec_command", {"cmd": "chmod -R 777 /"})
        self.assert_denied_or_permission_required(
            "exec_command",
            {
                "cmd": "python -c \"import urllib.request; urllib.request.urlopen('https://example.com', timeout=1)\"",
                "timeout_ms": 3000,
            },
        )

    def test_sensitive_environment_is_not_leaked_to_child_processes(self) -> None:
        result = self.client.call_tool(
            "exec_command",
            {
                "cmd": "python -c \"import os; print(os.environ.get('AWS_SECRET_ACCESS_KEY', ''))\"",
                "timeout_ms": 5000,
                "max_output_bytes": 4096,
            },
        )
        payload = self.assert_tool_success(result)
        self.assertEqual(payload.get("exit_code"), 0)
        self.assertNotIn("COMPLIANCE_SHOULD_NOT_LEAK", self.tool_text(result))

    def test_stdout_json_rpc_pollution_is_absent(self) -> None:
        stdout = self.client.stdout_snapshot()
        self.assertEqual(stdout, "", f"stdout must stay clean for JSON-RPC compatibility: {stdout!r}")

    def test_concurrent_read_only_tool_calls_are_stable(self) -> None:
        def call(index: int) -> str:
            with MCPClient(self.workspace.root, url=self.client.url) as client:
                if index % 2 == 0:
                    result = client.call_tool("read_file", {"path": "inside.txt"})
                else:
                    result = client.call_tool("search_text", {"query": "safe workspace", "path": "."})
                return self.tool_text(result)

        with ThreadPoolExecutor(max_workers=6) as executor:
            outputs = list(executor.map(call, range(12)))
        self.assertEqual(len(outputs), 12)
        self.assertTrue(all("safe workspace" in output for output in outputs))
