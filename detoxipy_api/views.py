# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import Message


class MessageListApiView(generics.ListCreateAPIView):
    """ Custom class for listing all of the messages
    """

    def get_queryset(self):
        """ Giving all chats from every user
        """
        return self.request


class MessageDetailApiView(generics.RetrieveAPIView):
    """ Class for accessing the detail for a single message
    """

    def get_queryset(self):
        """ Filters messages based on room in question
        """
        return Message.objects.filter(
            room__room_id=self.request.room.room_id
        )
