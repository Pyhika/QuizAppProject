# Generated by Django 3.1.6 on 2021-02-17 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0002_auto_20210216_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizmodel',
            name='images',
        ),
    ]
