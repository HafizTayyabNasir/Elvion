#!/bin/bash
set -o errexit

echo "--- Installing dependencies ONLY ---"
pip install -r requirements.txt

echo "--- Collecting static files ONLY ---"
python manage.py collectstatic --noinput --clear

echo "--- Minimal build complete. Migrations will be run manually. ---"