#!/bin/sh

# Ruun some setup tasks before starting the main application
echo "Setting up the environment..."

# Print the directory structure for debugging purposes
echo "File structure:"
tree

# Run the main application
echo "Starting the application..."
sh/bash poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
