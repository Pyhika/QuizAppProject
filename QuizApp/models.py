from django.db import models
from django.contrib.auth.models import User

TAG = [
    ('機械学習', 'Machine Learning'),
    ('ディープラーニング', 'Deep Learning'),
    ('データ分析', 'Data Analysis'),
    ('Python 基礎', 'Python Basic'),
]


class QuizModel(models.Model):
    postdate = models.DateField(auto_now_add=True)
    question = models.TextField()
    answer = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=20, choices=TAG)
