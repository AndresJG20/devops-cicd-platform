import os

VERSION = os.getenv("APP_VERSION","0.2.0")
PORT = int(os.getenv("PORT","8080"))
ENVIRONMENT = os.getenv("APP_ENV","development")
