import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from list.forms import ListForm, ListUpdateForm
from list.models import TodoList


@csrf_exempt
def todolists_page(request):
    todos = TodoList.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'list/list.html', context)


@csrf_exempt
def form_page(request):
    form = ListForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ListForm()
    context = {
        'form': form
    }
    return render(request, 'list/list_create.html', context)


@csrf_exempt
def form_update(request, id):
    form = ListUpdateForm(TodoList.objects.get(id=id).title)
    if form.is_valid():
        form.save()
        form = ListUpdateForm(TodoList.objects.get(id=id).title)
    context = {
        'form': form
    }
    return render(request, 'list/list_update.html', context)


@csrf_exempt
def create(request):
    todo_list = TodoList.objects.create(title=json.loads(request.body)['title'])
    todo_list.save()
    return build_response(TodoList.objects.get(id=todo_list.pk))


@csrf_exempt
def update(request):
    TodoList.objects.filter(id=json.loads(request.body)['id']).update(title=json.loads(request.body)['title'])
    return build_response(TodoList.objects.get(id=json.loads(request.body)['id']))


@csrf_exempt
def get_by_id(request, id):
    return build_response(TodoList.objects.get(id=id))


@csrf_exempt
def build_response(obj):
    return HttpResponse(
        serializers.serialize('json', [obj]),
        content_type="text/json-comment-filtered"
    )
