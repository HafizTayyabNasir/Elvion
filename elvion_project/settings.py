"""
Django settings for elvion_project project.
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ==============================================================================
# CORE PRODUCTION SETTINGS FOR VERCEL
# ==============================================================================

# SECRET_KEY is now read from an environment variable for security.
# You will set this in the Vercel dashboard.
# The second argument is a fallback key for local development.
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-y-nh96c1ncur+fkquj#howq067m81+c(p4o4)%znhj1&86$d7r')

# DEBUG is False in production for security, but True for local development.
# Vercel sets the 'VERCEL_ENV' variable to 'production' automatically.
DEBUG = os.environ.get('VERCEL_ENV') != 'production'

# Add your Vercel project URL to ALLOWED_HOSTS.
# The '.vercel.app' entry allows any subdomain of vercel.app, which is convenient.
ALLOWED_HOSTS = ['.vercel.app', '127.0.0.1']

# ==============================================================================
# Application definition
# ==============================================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Your apps
    'website.apps.WebsiteConfig',
    'chatbot.apps.ChatbotConfig',
    'appointments.apps.AppointmentsConfig'
]

# ==============================================================================
# MIDDLEWARE Configuration for Vercel
# ==============================================================================
# whitenoise middleware is added to serve static files in production.
# It must be placed right after the SecurityMiddleware.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "elvion_project.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = "elvion_project.wsgi.application"


# ==============================================================================
# Database
# ==============================================================================
# This default SQLite configuration is fine for Vercel deployment,
# but note that the database will be temporary and reset on new deployments.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ==============================================================================
# Password validation
# ==============================================================================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# ==============================================================================
# Internationalization
# ==============================================================================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# ==============================================================================
# Static files (CSS, JavaScript, Images) for Vercel
# ==============================================================================
STATIC_URL = 'static/'
# This tells Django where to find your static files in development.
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# This is where `collectstatic` will put all static files for production.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# This tells whitenoise to handle static file compression and caching.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ==============================================================================
# Default primary key field type
# ==============================================================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ==============================================================================
# Authentication Settings
# ==============================================================================
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'