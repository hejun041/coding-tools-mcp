from __future__ import annotations

from typing import Any

from tests.compliance.mcp_client import FORBIDDEN_TOOL_NAMES, FORBIDDEN_TOOL_TERMS, MCPError, REQUIRED_TOOLS
from tests.compliance.test_support import ComplianceTestCase


class MCPContractTests(ComplianceTestCase):
    def test_initialize_succeeds_and_tools_list_is_available(self) -> None:
        tools = self.client.list_tools()
        self.assertIsInstance(tools, list)
        self.assertGreater(len(tools), 0)

    def test_tools_list_contains_all_required_p0_tools(self) -> None:
        names = {tool.get("name") for tool in self.client.list_tools()}
        missing = sorted(set(REQUIRED_TOOLS) - names)
        self.assertEqual(missing, [], f"missing required P0 tools: {missing}")

    def test_tools_list_excludes_forbidden_product_layer_tools(self) -> None:
        names = {str(tool.get("name", "")) for tool in self.client.list_tools()}
        exact_forbidden = sorted(names & FORBIDDEN_TOOL_NAMES)
        self.assertEqual(exact_forbidden, [], f"forbidden tools exposed: {exact_forbidden}")
        term_hits = [
            name
            for name in names
            for term in FORBIDDEN_TOOL_TERMS
            if term in name.lower()
        ]
        self.assertEqual(term_hits, [], f"product-layer tool terms exposed: {sorted(term_hits)}")

    def test_each_tool_has_valid_basic_json_schema(self) -> None:
        for tool in self.client.list_tools():
            with self.subTest(tool=tool.get("name")):
                self.assertIsInstance(tool.get("name"), str)
                self.assertIsInstance(tool.get("description"), str)
                schema = tool.get("inputSchema")
                self.assert_schema_object(schema)

    def test_success_and_failure_paths_return_structured_tool_results(self) -> None:
        success = self.client.call_tool("read_file", {"path": "src/math.js"})
        payload = self.assert_tool_success(success)
        self.assertTrue(payload or self.tool_text(success))

        failure = self.assert_denied_or_permission_required("read_file", {"path": "../outside-secret.txt"})
        self.assertTrue(failure)

    def test_unknown_tool_returns_standard_json_rpc_error_or_tool_error(self) -> None:
        try:
            result = self.client.call_tool("definitely_not_a_tool", {})
        except MCPError as exc:
            self.assertIn(exc.error.get("code"), {-32601, -32602, -32000})
            self.assertIsInstance(exc.error.get("message"), str)
            return
        self.assertTrue(result.get("isError"), f"unknown tool must not succeed: {result!r}")

    def test_server_does_not_write_debug_logs_to_stdout(self) -> None:
        stdout = self.client.stdout_snapshot()
        self.assertEqual(stdout, "", f"server must log to stderr, not stdout: {stdout!r}")

    def assert_schema_object(self, schema: Any) -> None:
        self.assertIsInstance(schema, dict, f"inputSchema must be an object, got {schema!r}")
        self.assertEqual(schema.get("type"), "object", f"inputSchema.type must be object: {schema!r}")
        self.assertIsInstance(schema.get("properties", {}), dict)
        self.assert_schema_node(schema)

    def assert_schema_node(self, node: Any) -> None:
        if isinstance(node, dict):
            if "type" in node:
                allowed = {"array", "boolean", "integer", "null", "number", "object", "string"}
                value = node["type"]
                if isinstance(value, list):
                    self.assertTrue(set(value) <= allowed, f"invalid schema type list: {value!r}")
                else:
                    self.assertIn(value, allowed, f"invalid schema type: {value!r}")
            for key in ("properties", "$defs", "definitions"):
                for child in node.get(key, {}).values():
                    self.assert_schema_node(child)
            if "items" in node:
                self.assert_schema_node(node["items"])
            for key in ("anyOf", "oneOf", "allOf"):
                for child in node.get(key, []):
                    self.assert_schema_node(child)
