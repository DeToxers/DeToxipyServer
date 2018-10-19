from .views import MessagePostApiView, GetBubbleApiView, MessageGetApiView
from django.urls import path
from rest_framework.authtoken import views


urlpatterns = [
    path('api/v1/chat', MessagePostApiView.as_view(), name='post-message'),
    path('api/v1/chat/<int:pk>', MessageGetApiView.as_view(), name='get-message'),
    path('api/v1/bubble', GetBubbleApiView.as_view(), name='get-bubble'),
]
