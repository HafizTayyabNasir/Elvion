#!/bin/bash

# This script tells Vercel how to build your Django project.

# Exit immediately if a command exits with a non-zero status.
set -o errexit

# Install all the Python packages listed in your requirements.txt file.
# We use 'python3.11 -m pip' to be explicit and avoid 'pip: command not found' errors.
python3.11 -m pip install -r requirements.txt

# Collect all of Django's static files (CSS, JS, images) into a single folder.
# The '--noinput' flag prevents the command from asking for user confirmation.
python3.11 manage.py collectstatic --noinput

# Apply any pending database migrations.
python3.11 manage.py migrate