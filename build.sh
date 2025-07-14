#!/bin/bash
...
# 2. Apply Database Migrations
echo "--- Applying database migrations ---"
python manage.py migrate

# 3. Collect Static Files
# THIS IS THE COMMAND THAT FIXES THE ADMIN PANEL'S CSS
echo "--- Collecting static files ---"
python manage.py collectstatic --noinput --clear

echo "--- Build Complete ---"