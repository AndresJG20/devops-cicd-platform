# DeployLab — Platform Engineering
![CI](https://github.com/AndresJG20/devops-cicd-platform/actions/workflows/ci.yml/badge.svg)

A containerized reference service with request correlation, bounded-cardinality metrics, readiness/liveness endpoints, non-root execution, Prometheus configuration, local Kubernetes manifests and CI smoke checks.

## Local demo
```bash
docker compose up --build
python scripts/smoke.py
```
API: http://localhost:8080/docs. Prometheus: http://localhost:9090.

## Development
pip install -r requirements-dev.txt; python -m pytest -q.

## Delivery
CI tests, builds and launches the container for HTTP smoke checks. Kubernetes manifests enable a local deployment; continuous deployment to a remote environment is not configured. See [runbook](docs/runbook.md) for deployment, monitoring and rollback.
