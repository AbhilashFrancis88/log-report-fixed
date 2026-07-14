# log-report

A `dynamo` benchmark task: parse an Apache-style access log and emit a JSON
summary report.

## Task

See [instruction.md](instruction.md). Given `/app/access.log`, produce
`/app/report.json` containing `total_requests`, `unique_ips`, and `top_path`.

## Layout

- `task.toml` — task metadata and environment/verifier config.
- `environment/` — Dockerfile and the sample `access.log` used for the task.
- `solution/` — reference (oracle) solution (`solve.py` / `solve.sh`).
- `tests/` — verifier: `test_outputs.py` checks `report.json` against the
  expected ground truth, run via `test.sh`.
- `jobs/` — sample trial runs. The oracle solution scores `reward=1.0`; a
  no-op agent scores `reward=0.0`, confirming the verifier discriminates
  correctly.
