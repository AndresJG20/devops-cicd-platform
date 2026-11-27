# DeployLab — CI/CD Platform Demo
Servicio HTTP de ejemplo con endpoint de salud, pruebas, contenedor sin privilegios y pipeline CI. No es un sistema productivo de despliegue.

```bash
python -m unittest discover -v
python service.py
```
Abrir http://localhost:8080/health.

```bash
docker build -t deploylab .
docker run --rm -p 127.0.0.1:8080:8080 deploylab
```
GitHub Actions ejecuta pruebas y construye la imagen. No se configura un destino de despliegue remoto ni credenciales.
