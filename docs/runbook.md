# Guía de operación de DeployLab

## Verificación inicial

- GET /health: comprueba que el proceso responde.
- GET /ready: comprueba la disponibilidad del servicio sin estado. No verifica dependencias externas.
- GET /version: muestra la versión y el entorno configurados.
- X-Request-ID: permite relacionar una respuesta con su registro de ejecución.

## Monitoreo

Inicia Docker Compose y abre Prometheus en http://localhost:9090. En la sección de objetivos de monitoreo, comprueba que el servicio esté disponible. Genera varias solicitudes a la API y consulta:

```promql
sum(rate(http_requests_total[5m])) by (status)
```

La consulta agrupa la tasa de solicitudes por código HTTP. Las métricas se mantienen en memoria por proceso; para un despliegue de varias réplicas se necesita recolectar las métricas de cada una.

## Kubernetes local

Con Docker, kubectl y un clúster local kind disponibles, se puede intentar el siguiente recorrido:

```bash
docker build -t deploylab:local .
kind load docker-image deploylab:local
kubectl apply -f k8s/
kubectl rollout status deployment/deploylab
kubectl port-forward svc/deploylab 8080:8080
```

Desde otra terminal, ejecuta python scripts/smoke.py. Si el puerto 8080 está ocupado por Docker Compose, detén ese entorno primero.

## Reversión de cambios

Después de actualizar el despliegue a una imagen con una etiqueta diferente, Kubernetes permite consultar su historial y volver a una revisión previa:

```bash
kubectl rollout history deployment/deploylab
kubectl rollout undo deployment/deploylab
kubectl rollout status deployment/deploylab
```

Los límites de recursos y las comprobaciones de salud son valores de demostración. No se incluye un registro remoto de imágenes, Grafana, escaneo de vulnerabilidades ni un entorno productivo. La ejecución del clúster y el monitoreo visual requieren validación adicional.
