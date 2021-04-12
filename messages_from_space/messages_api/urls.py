from messages_api import views

from django.urls import path

urlpatterns = [
    path('', views.index),
    path('api/get_messages', views.unreadJson, name='get_messages'),
    path('api/mark_read', views.mkRead, name='mark_read'),
]