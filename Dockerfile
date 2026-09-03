# =========================================================
# GrantPulse AI — Production Dockerfile
# Optimized for Google Cloud Run, AWS ECS, & Render
# =========================================================

FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files into container
COPY . /app

# Install Python requirements
RUN pip install --no-cache-dir \
    requests \
    urllib3 \
    fastapi \
    uvicorn \
    stripe

# Expose server port
EXPOSE 8000

# Health check endpoint
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# Launch GrantPulse local server & API orchestrator
CMD ["python", "serve_grantpulse.py"]
