from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False #프로필 구현에서 수정 True->False

ALLOWED_HOSTS = ['43.200.177.42']


INSTALLED_APPS = list(DJANGO_APPS) + list(PROJECT_APPS)

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]