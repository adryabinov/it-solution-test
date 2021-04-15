from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
import json

from messages_api.models import MessageFromSpace

# Create your views here.


def index(request):
    return render(request, 'index.html', context={
        'who': 'World',
    })


def unread_json(request):
    messages = []
    for message in MessageFromSpace.objects.filter(read=False).order_by('-pk'):
        messages.append({
            'id': message.pk,
            'date': message.date,
            'text': message.text,
            'read': message.read})
    return JsonResponse(messages, safe=False)


def mk_read(request):
    read_id = request.GET.get('id')
    message = MessageFromSpace.objects.get(pk=read_id)
    message.read = True
    message.save()

    return HttpResponse('True')
