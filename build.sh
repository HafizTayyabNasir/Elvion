#!/bin/bash

# This script is the single source of truth for the build process.

# Exit on error
set -o errexit

# Install Python dependencies
echo "--- Installing Python dependencies ---"
pip install -r requirements.txt

# Create a directory for static files
mkdir -p staticfiles_build

# Run collectstatic
echo "--- Collecting static files ---"
python manage.py collectstatic --noinput --clear

# Run migrations
echo "--- Applying database migrations ---"
python manage.py migrate

# Create superuser
echo "--- Creating superuser ---"
python manage.py create_superuser_on_deploy