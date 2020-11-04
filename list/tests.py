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

    def test_get_all_lists(self):
        response = self.client.get('/list/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list/list.html')

    # def test_update_todolist_title(self):
    #     resp = self.client.post('/list/create/', {"title": "ex"})
    #     print(resp)
    #     response = self.client.put('/list/update/', {"id": "1", "title": "ex"})
    #     self.assertEqual(response.status_code, 200)

    # def test_call_view_fail_blank(self):
    #     response = self.client.post('/list/create/', {})
    #     self.assertFormError(response, 'form', 'title', 'This field is required.')
