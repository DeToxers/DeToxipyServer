# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import RecentMessage
from .models import Session
from datetime import datetime


class MessageListApiView(generics.ListCreateAPIView):
    """ Custom class for listing all of the messages
    """
    template_name = 'message_list.html'
    model = Session
    context_object_name = 'messages'
    queryset = Session.objects.all()

    def get_queryset(self):
        """ Giving all chats that we care about
        """
        target_time = datetime.today().timestamp() - 120
        return Session.objects.filter(
            room_id=self.request.room_id,
            time_updated__gte=datetime(target_time),
            weight__gt=0
        )

    def get_context_data(self, **kwargs):
        """
        """
        target_time = datetime.now()
        context = super().get_context_data(**kwargs)
        # do some stuff
        return context


class MessageDetailApiView(generics.RetrieveAPIView):
    """ Class for accessing the detail for a single message
    """

    def get_queryset(self):
        """ Filters messages based on room in question
        """
        return Message.objects.filter(
            room__room_id=self.request.room.room_id
        )
