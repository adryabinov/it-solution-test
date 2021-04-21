from django.test import TestCase
from django.test import Client
from django.http import JsonResponse
import json
from messages_api.models import MessageFromSpace


class ApiTestCase(TestCase):
    def setUp(self):
        MessageFromSpace.objects.create(pk=1, text='Test', is_read=False)
        MessageFromSpace.objects.create(pk=2, text='Test-T', is_read=True)

    def test_serialize(self):
        test_message = MessageFromSpace.objects.get(text='Test')
        self.assertEqual(
            MessageFromSpace.serialize(test_message)['id'], 1
        )
        self.assertEqual(
            MessageFromSpace.serialize(test_message)['text'], 'Test'
        )
        self.assertEqual(
            MessageFromSpace.serialize(test_message)['is_read'], False)

    def test_get_messages(self):
        test_message = MessageFromSpace.objects.get(text='Test')
        c = Client()
        resp = c.get('/api/get_messages?last_id=0')
        self.assertEqual(resp.content, JsonResponse([MessageFromSpace.serialize(test_message)], safe=False).content)

    def test_mark_read(self):
        c = Client(enforce_csrf_checks=True)
        resp = c.post('/api/mark_read?id=1')
        test_message = MessageFromSpace.objects.get(text='Test')
        self.assertEqual(MessageFromSpace.serialize(test_message)['is_read'], True)

