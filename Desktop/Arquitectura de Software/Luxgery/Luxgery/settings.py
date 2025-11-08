from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-replace-this-in-production"

DEBUG = True

ALLOWED_HOSTS = ["192.168.1.14", "localhost", "127.0.0.1"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "web",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",  # 👈 Para manejo de idiomas
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Luxgery.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "web", "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Luxgery.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = []

# 🌎 Configuración de idioma
LANGUAGE_CODE = "en"  # 👈 Por defecto inglés
USE_I18N = True
USE_L10N = True
USE_TZ = True
TIME_ZONE = "America/Bogota"

# 🗣️ Idiomas disponibles
LANGUAGES = [
    ("en", _("English")),
    ("es", _("Spanish")),
]

# 📁 Directorio donde se guardarán las traducciones
LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]

# 🖼️ Archivos estáticos
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "web", "static")]

# 📧 Configuración de correo
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "Luxgery.info@gmail.com"
EMAIL_HOST_PASSWORD = "PON_AQUI_TU_CONTRASEÑA_DE_APLICACIÓN"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
