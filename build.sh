#!/bin/bash

# Exit immediately if a command fails, which helps in debugging.
set -e

# --- 1. Install Dependencies ---
echo "STEP 1: Installing dependencies..."
pip install -r requirements.txt

# --- 2. Apply Database Migrations ---
# This creates the 'auth_user' table and all other tables.
# It uses the DATABASE_URL from your Vercel environment variables.
echo "STEP 2: Applying database migrations..."
python manage.py migrate

# --- 3. Create Superuser ---
# This runs the custom command to create your admin user.
# It also uses the environment variables from Vercel.
echo "STEP 3: Creating superuser (if it doesn't exist)..."
python manage.py create_superuser_on_deploy

# --- 4. Collect Static Files ---
# This gathers the CSS for the admin panel so it looks correct.
echo "STEP 4: Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "--- BUILD SUCCEEDED ---"