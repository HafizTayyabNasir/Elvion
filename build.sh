#!/bin/bash
set -o errexit

echo "--- Installing dependencies ---"
pip install -r requirements.txt

echo "--- Collecting static files ---"
python manage.py collectstatic --noinput --clear

echo "--- Applying database migrations ---"
python manage.py migrate

echo "--- Creating superuser (if it does not exist) ---"
python manage.py create_superuser_on_deploy

# ==========================================================
# THE CORRECTED LINE
# ==========================================================
echo "--- Setting/Resetting admin password ---"
python manage.py set_admin_password
# ==========================================================

echo "--- Build Complete ---"