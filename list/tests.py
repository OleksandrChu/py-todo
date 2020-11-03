from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from list.models import TodoList


class TodoListTest(TestCase):
    def create_todolist(self, title='do testing'):
        return TodoList.objects.create(title=title)

    def test_todolist_creation(self):
        t = self.create_todolist()
        self.assertTrue(isinstance(t, TodoList))
