# 本番環境
from .settings_common import *
import os
import dj_database_url

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['diary-quiz-app.herokuapp.com']

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
