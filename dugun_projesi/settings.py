# --- TEMEL AYARLAR ---
import os
from pathlib import Path
import cloudinary

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-test-key-123'
DEBUG = False # Yayında olduğumuz için False olmalı
ALLOWED_HOSTS = ['*'] # Render linkini buraya ekleyebilirsin

ROOT_URLCONF = 'dugun_projesi.urls'

# --- STATİK VE MEDYA AYARLARI ---
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Eğer STATICFILES_DIRS kullanıyorsan onu kaldırabilirsin, 
# çünkü artık dosyalar uygulamanın kendi içinde (App-level).
# Django, 'INSTALLED_APPS' içinde 'dugun_app' olduğu sürece 
# 'dugun_app/static' klasörünü otomatik tanır.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# --- ESKİ HALİ ---
# MEDIA_ROOT = BASE_DIR / 'media'
# settings.py dosyasında:
MEDIA_URL = '/'
# --- YENİ HALİ (Bunu kullan) --
# STORAGES ayarın modern standarttır, bunu kullan:
MEDIA_URL = 'https://res.cloudinary.com/bhgfroil/'

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# --- CLOUDINARY AYARLARI ---
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'bhgfroil',
    'API_KEY': '658135333859996',
    'API_SECRET': 'LUYhWBaxDSk8kJDC-VBYe5LNIUI',
}
cloudinary.config( 
  cloud_name = 'bhgfroil', 
  api_key = 'KENDI_API_KEY_BURAYA', 
  api_secret = 'KENDI_API_SECRET_BURAYA' 
)
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
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- DİĞERLERİ ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
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
CLOUDINARY_URL = 'cloudinary://658135333859996:LUYhWBaxDSk8kJDC-VBYe5LNIUI@bhgfroil'