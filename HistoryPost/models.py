from django.db import models
from django.contrib.auth.models import User

Category = [
    ('機械学習', 'Machine Learning'),
    ('ディープラーニング', 'Deep Learning'),
    ('データ分析', 'Data Analysis'),
    ('Python 基礎', 'Python Basic'),
]

class HistoryModel(models.Model):
    postdate = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    summary = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=Category)
