# Operations runbook
- Health: GET /health; readiness: GET /ready (stateless service).
- Version: GET /version; request correlation: X-Request-ID header.
- Metrics: GET /metrics, Prometheus at localhost:9090.
- Query: sum(rate(http_requests_total[5m])) by (status).
- Local Kubernetes: build deploylab:local, load it into a local cluster (e.g. kind load docker-image deploylab:local), apply k8s/, then kubectl port-forward svc/deploylab 8080:8080.
- Rollback: kubectl rollout undo deployment/deploylab after a versioned image update.
- Readiness and resource settings are illustrative. No remote cluster, registry, security scanner or Grafana instance has been deployed. Metrics are per process; Prometheus must scrape each replica for a real multi-replica deployment.
