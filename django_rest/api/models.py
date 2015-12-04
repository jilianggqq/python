from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Task(models.Model):
    completed = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    description = models.TextField()


class Info(models.Model):
    student_id = models.IntegerField(default=0)
    student_name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
