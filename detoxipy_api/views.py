# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Session
from datetime import datetime
from .serializers import MessageSerializer, ChatBotSerializer


class MessageListApiView(generics.ListAPIView):
    """ Custom class for listing all of the messages
    """
    # template_name = 'message_list.html'
    model = Session
    context_object_name = 'bubbles'
    serializer_class = MessageSerializer
    # queryset = Session.objects.all()
    pk_url_kwarg = 'id'

    def get_queryset(self):
        """ Getting all chats that we care about
        """
        max_bubble = 15
        top_stream_scores = Session.objects.filter(
            room_id=self.request.room_id).order_by(
                '-weight').values_list('weight', flat=True)
        top_records = Session.objects.order_by('-weight').filter(
            weight__in=top_stream_scores[:max_bubble])

        return top_records

        # target_time = datetime.now() - datetime.timedelta(minutes=2)
        # return Session.objects.filter(
        #     room_id=self.request.room_id,
        #     time_updated__gte=datetime(target_time),
        #     weight__gt=0
        # )

    def get_context_data(self, **kwargs):
        """
        """
        return RecentMessage.objects.filter(
            room__room_id=self.request.room.room_id
        )
        context = super().get_context_data(**kwargs)
        # do some stuff
        return context


class ChatBotCreateApiView(generics.CreateAPIView):
    """ This is what handles when the ChatBot sends up text
    """
    model = Session
    context_object_name = 'chat'
    serializer_class = ChatBotSerializer




# class MessageDetailApiView(generics.RetrieveAPIView):
#     """ Class for accessing the detail for a single message
#     """

#     def get_queryset(self):
#         """ Filters messages based on room in question
#         """
#         return Message.objects.filter(
#             room__room_id=self.request.room.room_id
#         )
