from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json

from messages_api.models import MessageFromSpace

# Create your views here.
def index(request):
    return render(request, 'index.html', context={
        'who': 'World',
    })

def unreadJson(request):
    res = serializers.serialize("json",MessageFromSpace.objects.filter(read=False).order_by('-pk'))
    return HttpResponse(res)

def mkRead(request):
    read_id = request.GET.get('id')
    message = MessageFromSpace.objects.get(pk=read_id)
    message.read = True
    message.save()

    return HttpResponse(serializers.serialize("json",MessageFromSpace.objects.filter(pk=read_id)))