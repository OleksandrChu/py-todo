from django.db import models

from list.models import TodoList


class Task(models.Model):
    title = models.CharField(max_length=250)
    list_id = models.IntegerField()
