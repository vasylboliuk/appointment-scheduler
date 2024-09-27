#!/bin/sh

# Run any commands before the app starts, like database migrations
# Example: poetry run alembic upgrade head

# Start the application
uvicorn src.main:app --reload