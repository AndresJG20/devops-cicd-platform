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
