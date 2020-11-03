from django.db import models


class TodoList(models.Model):
    title = models.CharField(max_length=30)
