from .base import *


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
