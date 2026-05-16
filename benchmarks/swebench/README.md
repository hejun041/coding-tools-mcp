# SWE-bench Smoke Regression

This directory contains the regression scaffolding for the benchmark path:

- `subsets/smoke-lite-10.json`: fixed SWE-bench Lite smoke subset.
- `predictions/baseline_native.jsonl`: schema-valid baseline predictions.
- `predictions/candidate_mcp.jsonl`: schema-valid candidate MCP predictions.
- `run_smoke.py`: preflight/report script and optional official harness launcher.

The checked-in prediction files are placeholders with empty patches. They are
valid JSONL inputs for the official harness, but they are not a meaningful
native-vs-MCP comparison until a real baseline runner and MCP runner generate
patches.

Preflight/report:

```bash
python benchmarks/swebench/run_smoke.py
```

Official evaluation, when Docker and `swebench` are available and real
predictions have been generated:

```bash
python benchmarks/swebench/run_smoke.py --run-evaluation
```
