# elvion_project/wsgi.py

import os
import sys
import subprocess
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "elvion_project.settings")

# This function will run our management commands
def run_management_commands():
    try:
        print("--- Vercel environment detected, running management commands ---")

        # Command 1: Apply migrations
        print("--- 1. Applying database migrations ---")
        migrate_result = subprocess.run(
            [sys.executable, "manage.py", "migrate", "--noinput"],
            capture_output=True, text=True, check=False
        )
        print(migrate_result.stdout)
        print(migrate_result.stderr)
        if migrate_result.returncode != 0:
            print("!!! MIGRATION FAILED !!!")
            return # Stop if migrations fail

        # Command 2: Create superuser
        print("--- 2. Creating superuser (if needed) ---")
        create_superuser_result = subprocess.run(
            [sys.executable, "manage.py", "create_superuser_on_deploy"],
            capture_output=True, text=True, check=False
        )
        print(create_superuser_result.stdout)
        print(create_superuser_result.stderr)

        # Command 3: Set/Reset admin password
        print("--- 3. Setting/Resetting admin password ---")
        set_password_result = subprocess.run(
            [sys.executable, "manage.py", "set_admin_password"],
            capture_output=True, text=True, check=False
        )
        print(set_password_result.stdout)
        print(set_password_result.stderr)

        print("--- Management commands finished ---")
    except Exception as e:
        print(f"!!! An unexpected error occurred during management commands: {e}")

# Run the commands only in the Vercel environment
if 'VERCEL' in os.environ:
    run_management_commands()

# Get the Django application
application = get_wsgi_application()
app = application