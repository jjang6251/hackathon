from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False #프로필 구현에서 수정 True->False

ALLOWED_HOSTS = ['3.35.27.125']


INSTALLED_APPS = list(DJANGO_APPS) + list(PROJECT_APPS)

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_ROOT = os.path.join(BASE_DIR, 'static')