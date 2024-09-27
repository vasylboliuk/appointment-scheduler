#!/bin/sh

# Start the application
echo "Start Application"
find ~/app/appointment-scheduler
exec "find ~/app/appointment-scheduler"
exec "$@"
exec "uvicorn src.main:app --reload"