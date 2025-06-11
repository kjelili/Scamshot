# Base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    clamav \ 
    clamav-daemon \
    && rm -rf /var/lib/apt/lists/*

# Copy application
WORKDIR /app
COPY requirements/prod.txt .
RUN pip install --no-cache-dir -r prod.txt

COPY . .

# Configure ClamAV
RUN freshclam && \
    chown -R clamav:clamav /var/lib/clamav

# Start services
CMD ["sh", "-c", "clamd && streamlit run app/main.py --server.port=8501 --server.address=0.0.0.0"]