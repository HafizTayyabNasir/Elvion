#!/bin/bash
set -o errexit

echo "--- Installing dependencies ---"
pip install -r requirements.txt

echo "--- Collecting static files ---"
python manage.py collectstatic --noinput --clear

echo "--- Applying database migrations ---"
python manage.py migrate

# Run our new command to create the superuser
echo "--- Creating superuser (if it does not exist) ---"
python manage.py create_superuser_on_deploy

echo "--- Build Complete ---"