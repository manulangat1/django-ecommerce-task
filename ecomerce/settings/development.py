from .base import *

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = "info@kipchirchirlangat.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Peleza task"
EMAIL_USE_TLS = True

DATABASES = {
    "default": {
        "ENGINE": env("POSTGRES_ENGINE"),
        "NAME": env("POSTGRES_NAME"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}


CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
]
