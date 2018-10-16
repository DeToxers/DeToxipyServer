from .views import MessageDetailApiView
from django.urls import path
from rest_framework.authtoken import views


urlpatterns = [
    path('bubble/<int:pk>', MessageDetailApiView.as_view(), name='message-detail'),
]
