import json

from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from todo.models import Task


@csrf_exempt
def create(request):
    response_body = json.loads(request.body)
    task = Task.objects.create(
        title=response_body['title'],
        list_id=response_body['list_id']
    )
    task.save()
    return build_response(Task.objects.get(id=task.pk))


@csrf_exempt
def update(request, id):
    Task.objects.update(title=json.loads(request.body)['title'])
    return build_response(Task.objects.get(id=id))


@csrf_exempt
def get_by_id(request, id):
    return build_response(Task.objects.get(id=id))


@csrf_exempt
def build_response(obj):
    return HttpResponse(
        serializers.serialize('json', [obj]),
        content_type="text/json-comment-filtered"
    )
