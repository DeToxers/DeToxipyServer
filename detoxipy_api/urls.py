from .views import MessagePostApiView, GetBubbleApiView
from django.urls import path
from rest_framework.authtoken import views


urlpatterns = [
    path('api/v1/chat', MessagePostApiView, name='post-message'),
    path('api/v1/bubble', GetBubbleApiView.as_view(), name='get-bubble'),
]
