import logging
import time
import uuid
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from .config import VERSION, ENVIRONMENT
from .metrics import Metrics

logger = logging.getLogger("uvicorn.error")

def create_app():
    app = FastAPI(title="DeployLab",version=VERSION)
    metrics = Metrics()

    @app.middleware("http")
    async def observe(request: Request, call_next):
        start = time.monotonic()
        request_id = str(uuid.uuid4())
        status = 500
        try:
            response = await call_next(request)
            status = response.status_code
            response.headers["X-Request-ID"] = request_id
            return response
        finally:
            route = request.scope.get("route")
            template = getattr(route,"path","unmatched")
            metrics.observe(template,status,time.monotonic()-start)
            logger.info("request_id=%s method=%s route=%s status=%s",request_id,request.method,template,status)

    @app.get("/health")
    def health():
        return {"status":"ok"}

    @app.get("/ready")
    def ready():
        return {"status":"ready"}

    @app.get("/version")
    def version():
        return {"version":VERSION,"environment":ENVIRONMENT}

    @app.get("/metrics",response_class=PlainTextResponse)
    def metrics_endpoint():
        return metrics.render()
    return app

app = create_app()
