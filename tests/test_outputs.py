import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")

# Ground truth for environment/access.log, computed independently of the
# solution: 6 requests, 3 distinct client IPs, /index.html requested 3 times
# (more than any other path).
EXPECTED = {
    "total_requests": 6,
    "unique_ips": 3,
    "top_path": "/index.html",
}


def test_report_exists():
    """The agent produced a report file."""
    assert REPORT_PATH.exists(), "no report.json found"


def test_report_is_valid_json_object():
    """The report is a JSON object with exactly the required keys."""
    with REPORT_PATH.open() as f:
        data = json.load(f)
    assert isinstance(data, dict), "report.json must contain a JSON object"
    assert set(data.keys()) == set(EXPECTED.keys()), (
        f"report.json must have exactly these keys: {sorted(EXPECTED)}, "
        f"got: {sorted(data.keys())}"
    )


def test_total_requests():
    data = json.loads(REPORT_PATH.read_text())
    assert data["total_requests"] == EXPECTED["total_requests"]


def test_unique_ips():
    data = json.loads(REPORT_PATH.read_text())
    assert data["unique_ips"] == EXPECTED["unique_ips"]


def test_top_path():
    data = json.loads(REPORT_PATH.read_text())
    assert data["top_path"] == EXPECTED["top_path"]
