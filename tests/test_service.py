from fastapi.testclient import TestClient
from service.main import create_app

def test_health_readiness_and_version():
    c=TestClient(create_app())
    r=c.get("/health")
    assert r.status_code==200 and r.json()=={"status":"ok"}
    assert r.headers["X-Request-ID"]
    assert c.get("/ready").json()["status"]=="ready"
    assert c.get("/version").json()["version"]

def test_metrics_cardinality():
    c=TestClient(create_app())
    for path in ("/missing-a","/missing-b","/health"):
        c.get(path)
    output=c.get("/metrics").text
    assert 'http_requests_total{route="unmatched",status="404"} 2' in output
    assert 'http_requests_total{route="/health",status="200"} 1' in output
    assert "missing-a" not in output


def test_duration_and_request_identifiers():
    client = TestClient(create_app())
    first = client.get("/health")
    second = client.get("/health")
    assert first.headers["X-Request-ID"] != second.headers["X-Request-ID"]
    result = client.get("/metrics")
    assert result.status_code == 200
    assert "version=0.0.4" in result.headers["content-type"]
    assert 'http_request_duration_seconds_count{route="/health"} 2' in result.text
    assert 'http_request_duration_seconds_sum{route="/health"}' in result.text
