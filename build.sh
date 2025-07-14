#!/bin/bash

# Exit immediately if a command fails.
set -e

echo "--- INSTALLING DEPENDENCIES ---"
pip install -r requirements.txt

echo "--- COLLECTING STATIC FILES ---"
python manage.py collectstatic --noinput --clear

echo "--- APPLYING DATABASE MIGRATIONS ---"
python manage.py migrate