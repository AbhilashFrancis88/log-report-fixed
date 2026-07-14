There is an Apache-style access log at `/app/access.log`. Parse it and write a
JSON summary report to `/app/report.json`.

Success criteria:

1. `/app/report.json` exists and contains a single JSON object with exactly
   these keys: `total_requests`, `unique_ips`, `top_path`.
2. `total_requests` (integer) is the total number of log lines (requests) in
   `/app/access.log`.
3. `unique_ips` (integer) is the number of distinct client IP addresses
   (first field of each log line) that appear in the log.
4. `top_path` (string) is the request path (e.g. `/index.html`) that appears
   most often across all requests.
