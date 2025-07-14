#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -o errexit

echo "--- Building Elvion Project ---"

# Upgrade pip and install packages
echo "--- Installing dependencies from requirements.txt ---"
python3.11 -m pip install --upgrade pip
python3.11 -m pip install -r requirements.txt

# Run database migrations
echo "--- Applying database migrations ---"
python3.11 manage.py migrate

# Collect static files
echo "--- Collecting static files ---"
python3.11 manage.py collectstatic --noinput --clear

echo "--- Build Complete ---"