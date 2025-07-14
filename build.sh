#!/bin/bash

# This script will be automatically run by the @vercel/python builder

# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Run our superuser creation script
python manage.py create_superuser_on_deploy

# Collect static files
python manage.py collectstatic --noinput --clear