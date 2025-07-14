#!/bin/bash

# This script tells Vercel how to build your Django project.

# Exit immediately if a command exits with a non-zero status.
set -o errexit

echo "--- Building Elvion Project ---"

# --- 1. Installation ---
# Install all Python packages from your requirements file.
echo "--- Installing dependencies ---"
pip install -r requirements.txt

# --- 2. Database Migrations ---
# This is the most important step. It creates all the tables
# (like auth_user) in your Postgres database.
echo "--- Applying database migrations ---"
python manage.py migrate

# --- 3. Collect Static Files ---
# This command gathers all CSS, JS, and images, including the
# files needed to style the Django admin panel.
echo "--- Collecting static files ---"
python manage.y collectstatic --noinput --clear

echo "--- Build Complete ---"