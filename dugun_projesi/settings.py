import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# VERİTABANI AYARLARI (Bu kısım eksik olduğu için hata alıyordun)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# settings.py dosyasının en altına yapıştır

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'bhgfroil',
    'API_KEY': '658135333859996',
    'API_SECRET': 'LUYhWBaxDSk8kJDC-VBYe5LNIUI',
}

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
SECRET_KEY = 'django-insecure-test-key-123'
DEBUG = True
ALLOWED_HOSTS = ['*']
# Uygulamalar (Burayı değiştirme)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dugun_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dugun_projesi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# Statik ve Medya Ayarları
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'dugun_app' / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Varsayılan birincil anahtar tipi
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Statik dosyaların (CSS, JS, Resimler) konumu
STATIC_URL = 'static/'

# Django'nun statik dosyaları nerede arayacağını belirtiyoruz
STATICFILES_DIRS = [
    BASE_DIR / 'dugun_app' / 'static',
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
