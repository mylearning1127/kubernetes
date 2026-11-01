FROM python:3.12-alpine
WORKDIR /app
COPY worker.py .
RUN adduser -D -u 10001 worker
USER 10001
CMD ["python", "-u", "worker.py"]
