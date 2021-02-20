# 本番環境
from .settings_common import *
import os

SECRET_KEY = '7*b73)j+4@41zrn2_6g#y!7x0#yu+fp5e$c=m-dc6esk0$yn01'
# SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['diary-quiz-app.herokuapp.com']

