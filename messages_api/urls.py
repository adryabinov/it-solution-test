from messages_api import views

from django.urls import path

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('api/get_messages', views.GetMessages.as_view(), name='get_messages'),
    path('api/mark_read', views.MarkRead.as_view(), name='mark_read'),
]