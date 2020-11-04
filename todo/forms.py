from django import forms

from list.models import TodoList
from todo.models import Task


class TaskCreateForm(forms.ModelForm):
    title = forms.CharField(label='Title',
                            widget=forms.TextInput(attrs={"placeholder": "eg. Gym training"}))

    class Meta:
        model = Task
        fields = ['title']
