PYTHON ?= python3
COMPLIANCE_RUNNER := PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -m tests.compliance.runner

.PHONY: compliance test-mcp-contract test-tool-golden test-security test-e2e test-codex-compat dogfood-mcp report

compliance:
	$(COMPLIANCE_RUNNER) --suite all --report

test-mcp-contract:
	$(COMPLIANCE_RUNNER) --suite mcp-contract --report

test-tool-golden:
	$(COMPLIANCE_RUNNER) --suite tool-golden --report

test-security:
	$(COMPLIANCE_RUNNER) --suite security --report

test-e2e:
	$(COMPLIANCE_RUNNER) --suite e2e --report

test-codex-compat:
	$(COMPLIANCE_RUNNER) --suite codex-compat --report

dogfood-mcp:
	$(COMPLIANCE_RUNNER) --suite dogfood --report

report:
	$(COMPLIANCE_RUNNER) --write-report-only
