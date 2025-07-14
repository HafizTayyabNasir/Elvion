"""
Django settings for elvion_project project.
"""
import os
from pathlib import Path
# Import the new library for database URLs
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ==============================================================================
# CORE PRODUCTION SETTINGS FOR VERCEL
# ==============================================================================

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-y-nh96c1ncur+fkquj#howq067m81+c(p4o4)%znhj1&86$d7r')
DEBUG = os.environ.get('VERCEL_ENV') != 'production'
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
# THE FINAL DATABASE CONFIGURATION
# ==============================================================================
# This logic checks if a POSTGRES_URL is available (on Vercel).
# If it is, it uses the Postgres database.
# If not (on your local machine), it falls back to using your local db.sqlite3 file.
# ==============================================================================
if 'POSTGRES_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.config(
            conn_max_age=600,
            conn_health_checks=True,
            # Use the pooled URL for better performance with serverless
            default=os.environ.get('POSTGRES_URL') 
        )
    }
else:
    # This is the database used for local development
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
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
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