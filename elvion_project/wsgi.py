# elvion_project/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "elvion_project.settings")

application = get_wsgi_application()

# ==============================================================================
# THE FIX: Vercel looks for an 'app' variable.
# We simply assign our existing 'application' to it.
# ==============================================================================
app = application
# ==============================================================================