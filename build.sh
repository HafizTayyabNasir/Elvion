#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -o errexit

echo "--- Building Elvion Project ---"

# --- Installation ---
echo "--- Installing dependencies ---"
pip install -r requirements.txt

# --- Build ---
# Collect static files first
echo "--- Collecting static files ---"
python manage.py collectstatic --noinput --clear

# Run database migrations using the POSTGRES_URL from Vercel's environment
echo "--- Applying database migrations to production database ---"
python manage.py migrate --database=default

echo "--- Build Complete ---"