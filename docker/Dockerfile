# Use the Python Alpine base image
FROM python:3.12-alpine

# Set the working directory
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.8.3
ENV POETRY_HOME="/opt/poetry"
ENV PATH=$PATH:$POETRY_HOME/bin
ENV APP_DIR="/app"
RUN echo $PATH

# Update and upgrade packages, install build dependencies
RUN apk update && apk upgrade && \
    apk add --no-cache gcc musl-dev libffi-dev openssl-dev bash curl

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Copy Poetry project files (pyproject.toml and poetry.lock) first for caching dependencies
COPY pyproject.toml poetry.lock $APP_DIR

# Install dependencies using Poetry (without dev dependencies)

RUN poetry --version
RUN poetry lock --no-update
RUN poetry install --no-root --only main
RUN poetry show uvicorn

# Copy the rest of the application code
COPY src/ $APP/src

# Copy the entrypoint script and give execution permission
COPY docker/entrypoint.sh $APP_DIR/entrypoint.sh
RUN chmod +x $APP_DIR/entrypoint.sh

# Expose the port (if your app runs on a specific port, adjust it)
EXPOSE 8000

# Set the entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]
