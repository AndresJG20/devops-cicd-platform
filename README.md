# DeployLab | Integración continua y operación de servicios

![Pruebas](https://github.com/AndresJG20/devops-cicd-platform/actions/workflows/ci.yml/badge.svg)

Proyecto de portafolio enfocado en el ciclo de entrega de un servicio web: desarrollo, pruebas, construcción de una imagen Docker, ejecución y monitoreo. El objetivo es reproducir localmente los pasos que permiten comprobar que una versión funciona antes de llevarla a otro entorno.

## Componentes

- API REST con FastAPI.
- Identificación de solicitudes mediante X-Request-ID.
- Endpoints de salud, disponibilidad y versión.
- Métricas de solicitudes y tiempos de respuesta con Prometheus.
- Imagen Docker ejecutada con un usuario sin privilegios.
- Manifiestos para un clúster Kubernetes local.
- Pruebas automatizadas y comprobaciones HTTP del contenedor mediante GitHub Actions.

## Ejecución local

Con Docker y Docker Compose instalados, abre una terminal en la raíz del repositorio.

```bash
docker compose up -d --build
python scripts/smoke.py
```

| Recurso | Dirección |
| --- | --- |
| Documentación de la API | http://localhost:8080/docs |
| Estado del servicio | http://localhost:8080/health |
| Métricas | http://localhost:8080/metrics |
| Prometheus | http://localhost:9090 |

Para detener los servicios:

```bash
docker compose down
```

## Desarrollo sin Docker

Con Python 3.12 instalado, desde PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m pytest -q
python -m uvicorn service.main:app --port 8080
```

## Integración continua

El flujo de GitHub Actions instala las dependencias, ejecuta pytest, construye la imagen, inicia un contenedor y comprueba los endpoints de salud y disponibilidad. Finalmente elimina el contenedor de prueba.

## Organización

| Carpeta | Contenido |
| --- | --- |
| service/ | API, configuración y métricas |
| tests/ | Pruebas de endpoints y agrupación de métricas |
| scripts/ | Comprobación HTTP del servicio |
| observability/ | Configuración de Prometheus |
| k8s/ | Manifiestos de despliegue y servicio |
| .github/workflows/ | Automatización de integración continua |
| docs/ | Guía de operación |

## Alcance

Se trata de una demostración local. El pipeline comprueba la integración y la ejecución de la imagen, pero no realiza despliegues automáticos en un servidor remoto. Los manifiestos Kubernetes están preparados para una prueba local y no se ha validado un clúster real.

Consulta la [guía de operación](docs/runbook.md) para conocer los pasos de monitoreo, despliegue local y reversión de versiones.
