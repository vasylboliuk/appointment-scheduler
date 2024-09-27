#!/bin/sh

# Run any commands before the app starts, like database migrations
# Example: poetry run alembic upgrade head

# Start the application
exec "find ~/repos/appointment-scheduler"
exec "$@"
exec "uvicorn src.main:app --reload"