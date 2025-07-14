# elvion_project/wsgi.py

import os
import sys
import subprocess
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "elvion_project.settings")

# ==============================================================================
# RUN MIGRATIONS ON STARTUP
# This is the guaranteed fix. It runs inside the live Vercel environment
# which has access to the database credentials.
# ==============================================================================
try:
    # Check if this is running on Vercel.
    if 'VERCEL' in os.environ:
        print("--- Vercel environment detected, attempting to apply migrations ---")
        
        # Use subprocess to call the manage.py migrate command.
        # This is more reliable than calling it directly from here.
        result = subprocess.run(
            [sys.executable, "manage.py", "migrate", "--noinput"],
            capture_output=True,
            text=True,
            check=False # Do not raise exception on failure, just log it
        )

        # Print the output to the Vercel logs for debugging
        print("--- Migration stdout ---")
        print(result.stdout)
        print("--- Migration stderr ---")
        print(result.stderr)
        
        if result.returncode == 0:
            print("--- Migrations applied successfully ---")
        else:
            print("!!! MIGRATION FAILED !!! See logs above.")

except Exception as e:
    print(f"!!! An unexpected error occurred during the migration attempt: {e}")
# ==============================================================================


application = get_wsgi_application()

# Vercel looks for this 'app' variable.
app = application