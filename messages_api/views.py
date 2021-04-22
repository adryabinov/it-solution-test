from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views import View
from messages_api.models import MessageFromSpace


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = {
            'title': 'сообщения из космоса',
            'page_title': 'СООБЩЕНИЯ ИЗ КОСМОСА'
        }
        return context


class GetMessages(View):
    def get(self, request):
        messages = [MessageFromSpace.serialize(message) for message
                    in
                    MessageFromSpace.objects.filter(is_read=False).order_by(
                        '-pk')]
        return JsonResponse(messages, safe=False)


class MarkRead(View):
    def post(self, request):
        read_id = request.GET.get('id')
        message = MessageFromSpace.objects.get(pk=read_id)
        message.is_read = True
        message.save()

        return JsonResponse(MessageFromSpace.serialize(message), safe=False)
