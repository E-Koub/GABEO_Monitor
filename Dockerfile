# --- Stage 1: Builder ---
FROM python:3.11-slim AS builder

WORKDIR /app
COPY setup.py .

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir  -e .

COPY . .

# --- Stage 2: Runtime ---
FROM jupyter/base-notebook:python-3.11

USER root

# Copier uniquement les packages installés
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copier les fichiers de l'app
COPY . /app
WORKDIR /app

ENV PYTHONPATH=/app

# Droits non root pour Jupyter et Streamlit
USER jovyan

EXPOSE 8501
EXPOSE 8888

CMD ["streamlit", "run", "public/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
