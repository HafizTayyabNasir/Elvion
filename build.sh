#!/bin/bash

# This script tells Vercel how to build your Django project.

# Exit immediately if a command exits with a non-zero status.
set -o errexit

# The Vercel Python builder automatically creates and activates a
# virtual environment, so we can now use 'pip' and 'python' directly.

# Upgrade pip
pip install --upgrade pip

# Install all the Python packages
pip install -r requirements.txt

# Collect all of Django's static files
python manage.py collectstatic --noinput

# Apply any pending database migrations
python manage.py migrate