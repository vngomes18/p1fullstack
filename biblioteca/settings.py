"""
Configurações do projeto "biblioteca".

Baseado no conteúdo da Aula 4 (Django I: projeto, models, ORM e Admin) e
Aula 5 (Django II: views, URLs, templates e forms) da disciplina
Laboratório de Programação Full Stack.
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env (nunca versionado no Git)
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: mantenha a SECRET_KEY em segredo em produção!
SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'django-insecure-troque-esta-chave-em-producao'
)

# SECURITY WARNING: nunca rode com DEBUG=True em produção!
DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'acervo',  # nosso app
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

ROOT_URLCONF = 'biblioteca.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # pasta de templates compartilhados (ex.: base.html)
        'DIRS': [BASE_DIR / 'acervo' / 'templates'],
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

WSGI_APPLICATION = 'biblioteca.wsgi.application'

# Banco de dados
# Por padrão usa SQLite (funciona sem instalar nada extra).
# Para usar PostgreSQL como na Aula 4, defina USE_POSTGRES=True no .env
# e preencha DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT.
if os.getenv('USE_POSTGRES', 'False') == 'True':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME', 'biblioteca_db'),
            'USER': os.getenv('DB_USER', 'postgres'),
            'PASSWORD': os.getenv('DB_PASSWORD', ''),
            'HOST': os.getenv('DB_HOST', 'localhost'),
            'PORT': os.getenv('DB_PORT', '5432'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'acervo' / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
