ARG PYTHON_VERSION=3.13.3
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting and logs due to buffering.
# Ensures logs are flushed immediately
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Set PYTHONPATH environment
ENV PYTHONPATH=/app

# Create a non-privileged user that the app will run under.
ARG UID=1000
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/home/appuser" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser && \
    mkdir -p /home/appuser && \
    chown appuser:appuser /home/appuser

# Copy requirements into the image
COPY requirements.txt .

# Install dependencies using copied file
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r requirements.txt

# Copy source code into the container
COPY . .

# Switch to the non-privileged user to run the application
USER appuser

# Expose the port that the application listens on.
EXPOSE 8080

# Run the application
CMD streamlit run src/app.py --server.port=8080 --server.address=0.0.0.0