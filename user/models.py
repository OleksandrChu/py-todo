from django.db import models

from list.models import TodoList


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    list_id = models.ForeignKey(TodoList, on_delete=models.CASCADE)