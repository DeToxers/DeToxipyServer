from .views import MessageListApiView
from django.urls import path
from rest_framework.authtoken import views


urlpatterns = [
    path('api/v1/chat', MessageListApiView.as_view(), name='message_list'),
    path('api/v1/bubble/<pk:id>', MessageListApiView.as_view(), name='message_list'),
]
