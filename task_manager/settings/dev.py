from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DJANGO_DEBUG", "False").lower() in ("true", "1")

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "planner-application.onrender.com",
    os.getenv("RENDER_EXTERNAL_HOSTNAME", ""),
]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
