# 本番環境
from .settings_common import *
import os

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['diary-quiz-app.herokuapp.com']

