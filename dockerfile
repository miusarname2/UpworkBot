# Dockerfile
FROM python:3.11-slim

# variables útiles
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copia todo el proyecto
COPY . /app

# puerto que Cloud Run proporcionará; uvicorn lo leerá desde $PORT
ENV PORT=8080

# Entrypoint: Uvicorn sirve la FastAPI (app:app)
CMD exec uvicorn src.webhook:app --host 0.0.0.0 --port ${PORT}
