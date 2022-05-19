import os

import dj_database_url
from distutils.util import strtobool
from dotenv import load_dotenv
from environs import Env

load_dotenv()
env = Env()
env.read_env()

DEFAULT_DATABASE_URL = f'{os.getenv("DB_ENGINE")}://{os.getenv("USER")}:' \
                      f''f'{os.getenv("PASSWORD")}@{os.getenv("HOST")}:' \
                      f''f'{os.getenv("PORT")}/{os.getenv("NAME")}'

DATABASES = {
    'default': dj_database_url.config(default=DEFAULT_DATABASE_URL)
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('SECRET_KEY', default='easy_key')

DEBUG = bool(strtobool(os.getenv('DEBUG', default='FALSE')))


ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default='*')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', default='ru-ru')

TIME_ZONE = os.getenv('TIME_ZONE', default='Europe/Moscow')

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
