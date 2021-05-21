import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from .models import Message
from .serializers import MessageSerializer


class MessageViewTestCase(APITestCase):

    def setUp(self):
        obj = Message.objects.create(text='tests are very important')


    def test_message_view_get(self):
        response = self.client.get(reverse("view-message", kwargs={"message_id": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_message_view_404(self):
        response = self.client.get(reverse("view-message", kwargs={"message_id": 9999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_message_view_put(self):
        response = self.client.put(reverse("view-message", kwargs={"message_id": 1}), 
                                           {"text": "bruh"}, content_type='application/json')
        obj = Message.objects.get(id=1)
        self.assertEqual(obj.text, "bruh")
    
    def test_message_view_delete(self):
        response = self.client.delete(reverse("view-message", kwargs={"message_id": 1}))
        self.assertEqual(len(Message.objects.all()), 0)

class MessageCreateViewCase(APITestCase):
    
    def test_create_view(self):
        response =  self.client.post(reverse("create-message"), {"text": "ok, tested"}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
