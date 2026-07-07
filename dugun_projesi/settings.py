# --- TEMEL AYARLAR ---
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-test-key-123'
DEBUG = False # Yayında olduğumuz için False olmalı
ALLOWED_HOSTS = ['*'] # Render linkini buraya ekleyebilirsin

ROOT_URLCONF = 'dugun_projesi.urls'

# --- STATİK VE MEDYA AYARLARI ---
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'dugun_app' / 'static']

# --- ESKİ HALİ ---
MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# --- YENİ HALİ (Bunu kullan) ---
MEDIA_URL = 'https://res.cloudinary.com/bhgfroil/'

# --- STORAGE AYARLARI (Modern Yöntem) ---
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# --- CLOUDINARY AYARLARI ---
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'bhgfroil',
    'API_KEY': '658135333859996',
    'API_SECRET': 'LUYhWBaxDSk8kJDC-VBYe5LNIUI',
}

# --- VERİTABANI AYARLARI ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- MIDDLEWARE (WhiteNoise en üstlerde olmalı) ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Statik dosyaları sunar
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- DİĞERLERİ ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'dugun_app',
]

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

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'