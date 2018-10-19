from .views import MessagePostApiView
from django.urls import path
from rest_framework.authtoken import views


urlpatterns = [
    path('api/v1/bubble', MessagePostApiView.as_view(), name='get-bubble'),
]
