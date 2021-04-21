from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView
from messages_api.models import MessageFromSpace

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"


def unread_json(request):
    messages = [MessageFromSpace.serialize(message) for message
                in MessageFromSpace.objects.filter(is_read=False).order_by('-pk')]
    return JsonResponse(messages, safe=False)


def mk_read(request):
    read_id = request.GET.get('id')
    message = MessageFromSpace.objects.get(pk=read_id)
    message.is_read = True
    message.save()

    return JsonResponse(MessageFromSpace.serialize(message), safe=False)
