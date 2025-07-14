#!/bin/bash

# Exit on error
set -o errexit

# --- Installation ---
echo "--- Installing dependencies ---"
pip install -r requirements.txt

# --- Build ---
echo "--- Running migrations ---"
python manage.py migrate

echo "--- Collecting static files ---"
python manage.py collectstatic --noinput --clear

echo "--- Build Complete ---"