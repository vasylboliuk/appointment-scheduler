# Use the Python Alpine base image
FROM python:3.10-alpine

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.4.2 \
    POETRY_HOME="/opt/poetry"

# Update and upgrade packages, install build dependencies
RUN apk update && apk upgrade && \
    apk add --no-cache gcc musl-dev libffi-dev openssl-dev bash curl

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set the working directory
WORKDIR /app

# Copy Poetry project files (pyproject.toml and poetry.lock) first for caching dependencies
COPY pyproject.toml poetry.lock /app/

# Install dependencies using Poetry (without dev dependencies)
RUN poetry install --no-root --no-dev

# Copy the rest of the application code
COPY src/ /app/

# Copy the entrypoint script and give execution permission
COPY docker/entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expose the port (if your app runs on a specific port, adjust it)
EXPOSE 8000

# Set the entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]

# Command to run the app (example: running the app with uvicorn)
CMD ["poetry", "run", "python", "main.py"]
