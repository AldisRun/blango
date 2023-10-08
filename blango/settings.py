import os, dj_database_url
import mimetypes
from pathlib import Path
from configurations import Configuration, values

mimetypes.add_type("text/css", ".css", True)

class Dev(Configuration):
  # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
  BASE_DIR = Path(__file__).resolve().parent.parent

  # SECURITY WARNING: keep the secret key used in production secret!
  SECRET_KEY = 'django-insecure-18my@44=5*gpmb1grcg#@1^6c5bsd6#r4pmln9z8k*rl2xpz2v'

  INTERNAL_IPS = ["192.168.11.179", "192.168.17.65", "172.20.10.3"]

  # SECURITY WARNING: don't run with debug turned on in production!
  DEBUG = values.BooleanValue(True)

  ALLOWED_HOSTS = values.ListValue(["localhost", "0.0.0.0", ".codio.io"])
  X_FRAME_OPTIONS = 'ALLOW-FROM ' + os.environ.get('CODIO_HOSTNAME') + '-8000.codio.io'
  CSRF_COOKIE_SAMESITE = None
  CSRF_TRUSTED_ORIGINS = ['https://' + os.environ.get('CODIO_HOSTNAME') + '-8000.codio.io']
  CSRF_COOKIE_SECURE = True
  SESSION_COOKIE_SECURE = True
  CSRF_COOKIE_SAMESITE = 'None'
  SESSION_COOKIE_SAMESITE = 'None'

  ACCOUNT_USER_MODEL_USERNAME_FIELD = None
  ACCOUNT_EMAIL_REQUIRED = True
  ACCOUNT_USERNAME_REQUIRED = False
  ACCOUNT_AUTHENTICATION_METHOD = "email"

  # Application definition
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.sites',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'blango_auth',
      'blog',
      'crispy_forms',
      'crispy_bootstrap5',
      'debug_toolbar',
      'rest_framework.authtoken',
      'rest_framework',
      'allauth',
      'allauth.account',
      'allauth.socialaccount',
      'allauth.socialaccount.providers.google',
      'drf_yasg',
  ]
  
  SWAGGER_SETTINGS = {
      "SECURITY_DEFINITIONS": {
          "Token": {"type": "apiKey", "name": "Authorization", "in": "header"},
          "Basic": {"type": "basic"},
      }
  }

  MIDDLEWARE = [
      'debug_toolbar.middleware.DebugToolbarMiddleware',
      'django.middleware.security.SecurityMiddleware',
      'django.contrib.sessions.middleware.SessionMiddleware',
      'django.middleware.common.CommonMiddleware',
  #    'django.middleware.csrf.CsrfViewMiddleware',
      'django.contrib.auth.middleware.AuthenticationMiddleware',
      'django.contrib.messages.middleware.MessageMiddleware',
  #    'django.middleware.clickjacking.XFrameOptionsMiddleware',
  ]

  ACCOUNT_EMAIL_VERIFICATION = True

  REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly"
    ],
  }

  SITE_ID = 1

  EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

  ACCOUNT_ACTIVATION_DAYS = 7
  
  REGISTRATION_OPEN = True

  AUTH_USER_MODEL = "blango_auth.User"

  CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

  CRISPY_TEMPLATE_PACK = "bootstrap5"

  ROOT_URLCONF = 'blango.urls'

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
                  # 'blango.context_processors.settings',      # Add
                  # 'social_django.context_processors.backends',  # Add
                  # 'social_django.context_processors.login_redirect', # Add
              ],
          },
      },
  ]

  WSGI_APPLICATION = 'blango.wsgi.application'

  # Database
  # https://docs.djangoproject.com/en/4.0/ref/settings/#databases
  DATABASES = {
    "default": dj_database_url.config(default=f"sqlite:///{BASE_DIR}/db.sqlite3"),
    "alternative": dj_database_url.config(
        "ALTERNATIVE_DATABASE_URL",
        default=f"sqlite:///{BASE_DIR}/alternative_db.sqlite3",
    ),
  }

  # Password validation
  # https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
  AUTH_PASSWORD_VALIDATORS = [
      {
          'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
      },
      {
          'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
      },
      {
          'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
      },
      {
          'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
      },
  ]

  # Internationalization
  # https://docs.djangoproject.com/en/4.0/topics/i18n/
  LANGUAGE_CODE = 'en-us'
  TIME_ZONE = values.Value('UTC')
  USE_I18N = True
  USE_L10N = True
  USE_TZ = True

  # Static files (CSS, JavaScript, Images)
  # https://docs.djangoproject.com/en/4.0/howto/static-files/
  STATIC_ROOT = os.path.join(BASE_DIR, 'static')
  STATIC_URL = 'static/'

  # Default primary key field type
  # https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
  DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
  CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
  CRISPY_TEMPLATE_PACK = "bootstrap5"
  
  LOGGING = {
      "version": 1,
      "disable_existing_loggers": False,
      "filters": {
          "require_debug_false": {
              "()": "django.utils.log.RequireDebugFalse",
          },
      },
      "formatters": {
          "verbose": {
              "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
              "style": "{",
          },
      },
      "handlers": {
          "console": {
              "class": "logging.StreamHandler",
              "stream": "ext://sys.stdout",
              "formatter": "verbose",
          },
          "mail_admins": {
              "level": "ERROR",
              "class": "django.utils.log.AdminEmailHandler",
              "filters": ["require_debug_false"],
          },
      },
      "loggers": {
          "django.request": {
              "handlers": ["mail_admins"],
              "level": "ERROR",
              "propagate": True,
          },
      },
      "root": {
          "handlers": ["console"],
          "level": "DEBUG",
      },
  }
  PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
  ]

class Prod(Dev):
  DEBUG = False
  SECRET_KEY = values.SecretValue()
  AUTH_USER_MODEL = "blango_auth.User"
