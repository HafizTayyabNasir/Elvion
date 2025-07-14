#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -o errexit

echo "--- Building Elvion Project ---"

# --- Installation ---
echo "--- Installing dependencies ---"
pip install -r requirements.txt

# --- Collect Static Files ONLY ---
echo "--- Collecting static files ---"
python manage.py collectstatic --noinput --clear

echo "--- Build Complete ---"