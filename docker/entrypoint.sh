#!/bin/sh

# Ruun some setup tasks before starting the main application
echo "Setting up the environment..."

# Print the directory structure for debugging purposes
echo "File structure:"
find /app

# Run the main application
echo "Starting the application..."
exec poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
