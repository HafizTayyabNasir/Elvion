import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ==============================================================================
# CORE PRODUCTION SETTINGS FOR VERCEL
# ==============================================================================
SECRET_KEY = os.environ.get('SECRET_KEY')
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
    "whitenoise.runserver_nostatic", # For serving static files
    "django.contrib.staticfiles",
    # Your apps
    'website.apps.WebsiteConfig',
    'chatbot.apps.ChatbotConfig',
    'appointments.apps.AppointmentsConfig'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware", # For serving static files
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
# Database Configuration
# ==============================================================================
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('POSTGRES_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}
# Fallback to SQLite for local development if the database URL is not set
if 'POSTGRES_URL' not in os.environ:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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
# Static files (CSS, JavaScript, Images)
# ==============================================================================
STATIC_URL = 'static/'
# This tells Django where to find your static files in development.
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# THE CRITICAL CHANGE IS HERE: This path must match the 'distDir' in vercel.json
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build')

# This tells whitenoise to handle static file compression and caching.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ==============================================================================
# Default primary key field type & Auth Settings
# ==============================================================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'