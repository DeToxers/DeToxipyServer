# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .models import Session, RecentMessage
from datetime import datetime
from .serializers import MessageSerializer, ChatBotSerializer
from django.http import Http404

from rest_framework.response import Response
from rest_framework.request import clone_request
from rest_framework import status


class GetBubbleApiView(generics.ListAPIView):
    """ Custom class for listing all of the messages
    """
    # template_name = 'message_list.html'
    model = Session
    context_object_name = 'bubble'
    serializer_class = MessageSerializer
    # queryset = Session.objects.all()
    pk_url_kwarg = 'id'

    def get_queryset(self):
        """ Getting all chats that we care about
        """
        max_bubble = 5
        top_stream_scores = Session.objects.filter(
            room_id=self.request.room_id).order_by(
                'weight')[:max_bubble]
        # top_records = Session.objects.order_by('-weight').filter(
        #     weight__in=top_stream_scores[:max_bubble])

        json_to_return = self.format_query(top_stream_scores)

        return json_to_return

    def get_context_data(self, **kwargs):
        """ Filter messages by room id
        """
        return RecentMessage.objects.filter(
            room__room_id=self.request.room.room_id
        )
        context = super().get_context_data(**kwargs)
        return context

    def format_query(self, query):
        """ Creates a new formatted object for each max row so that D3 can read it and render a bubble chart

            Input:
                A queryset from our RecentMessage table

            Output:
                A list of dictionaries
        """
        bubble_data = []
        for row in query:
            obj = {}
            obj['name'] = row.content
            obj['size'] = row.weight
            bubble_data.append(obj)
        return bubble_data


class MessagePostApiView(generics.CreateAPIView):
    """ This is what handles when the ChatBot sends up text
    """
    model = Session
    context_object_name = 'chat'
    serializer_class = ChatBotSerializer

    # def post(self, request):
    #     """ Takes in live chat data and posts it into the db

    #     Input: request is a Django Request object

    #     Output: response, a Django Response object. In addition the cleaned
    #     words will be added to our database.

    #     """
    #     if request.method != 'POST':
    #         return generics.response(status=404)
    #     cleaned_words = self.sanitize(request.data.content)

    def update(self, request, *args, **kwargs):
        """
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object_or_none()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        if instance is None:
            lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
            lookup_value = self.kwargs[lookup_url_kwarg]
            extra_kwargs = {self.lookup_field: lookup_value}
            serializer.save(**extra_kwargs)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        serializer.save()
        return Response(serializer.data)

    def get_object_or_none(self):
        """
        """
        try:
            return self.get_object()
        except Http404:
            if self.request.method == 'PUT':
                # For PUT-as-create operation, we need to ensure that we have
                # relevant permissions, as if this was a POST request.  This
                # will either raise a PermissionDenied exception, or simply
                # return None.
                self.check_permissions(clone_request(self.request, 'POST'))
            else:
                # PATCH requests where the object does not exist should still
                # return a 404 response.
                raise

    def sanitize(self, raw_chat):
        """ TODO: Formats the raw chat to put in the db, also filters out filler words
            Input: raw chat which is a list

            Output: clean chat which is a dict
        """
        cleaned_words = {}
        for message in raw_chat:
            for word in message:
                if cleaned_words[word]:
                    cleaned_words[word] += 1
                else:
                    cleaned_words[word] = 1
        return cleaned_words
