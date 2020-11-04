from django import forms

from list.models import TodoList


class ListCreateForm(forms.ModelForm):
    title = forms.CharField(label='Title',
                            widget=forms.TextInput(attrs={"placeholder": "eg. Gym training"}))

    class Meta:
        model = TodoList
        fields = ['title']


class ListUpdateForm(forms.ModelForm):
    title = forms.CharField(label='Title')

    def __init__(self, title):
        super(ListUpdateForm, self).__init__()
        self.fields["title"].initial = title

    class Meta:
        model = TodoList
        fields = ['title']
