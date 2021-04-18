from messages_api import views

from django.urls import path

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('api/get_messages', views.unread_json, name='get_messages'),
    path('api/mark_read', views.mk_read, name='mark_read'),
]