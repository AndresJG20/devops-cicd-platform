FROM python:3.12-slim
WORKDIR /app
COPY service.py .
USER 10001:10001
EXPOSE 8080
HEALTHCHECK CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/health')"
CMD ["python","service.py"]
