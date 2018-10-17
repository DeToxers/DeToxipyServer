# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from collections import Counter
from rest_framework import generics

from .models import Session
from datetime import datetime
from .serializers import MessageSerializer, ChatBotSerializer
from django.http import Http404

# from django.views.decorators.cache import cache_page
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

    def get_queryset(self, *args, **kwargs):
        """ Getting all chats that we care about
        """
        max_bubble = 5
        top_stream_scores = Session.objects.filter(
            room_id=self.request.room_id).order_by(
                'weight')[:max_bubble]
        # top_records = Session.objects.order_by('-weight').filter(
        #     weight__in=top_stream_scores[:max_bubble])

        import pdb; pdb.set_trace()
        return top_stream_scores

    def post(self, *args, **kwargs):
        """
        """
        pass


    # def get_context_data(self, **kwargs):
    #     """ Filter messages by room id
    #     """
    #     return RecentMessage.objects.filter(
    #         room__room_id=self.request.room.room_id
    #     )
    #     context = super().get_context_data(**kwargs)
    #     return context

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
    # model = Session
    serializer_class = ChatBotSerializer

    def get(self, *args, **kwargs):
        """
        """
        # import pdb; pdb.set_trace()
        queryset = Session.objects.all()

        return Response(queryset)



    # # def post(self, request):
    # #     """ Takes in live chat data and posts it into the db

    # #     Input: request is a Django Request object

    # #     Output: response, a Django Response object. In addition the cleaned
    # #     words will be added to our database.

    # #     """
    # #     if request.method != 'POST':
    # #         return generics.response(status=404)
    # #     cleaned_words = self.sanitize(request.data.content)

    # def update(self, request, **kwargs):
    #     """
    #     """
    #     instance = self.get_object_or_none()
    #     serializer = self.serializer_class

    #     if instance is None:
    #         lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
    #         lookup_value = self.kwargs[lookup_url_kwarg]
    #         extra_kwargs = {self.lookup_field: lookup_value}
    #         serializer.save(**extra_kwargs)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     serializer.save()
    #     return Response(serializer.data)

    # def get_object_or_none(self):
    #     """
    #     """
    #     try:
    #         return self.get_object()
    #     except Http404:
    #         if self.request.method == 'PUT':
    #             # For PUT-as-create operation, we need to ensure that we have
    #             # relevant permissions, as if this was a POST request.  This
    #             # will either raise a PermissionDenied exception, or simply
    #             # return None.
    #             self.check_permissions(clone_request(self.request, 'POST'))
    #         else:
    #             # PATCH requests where the object does not exist should still
    #             # return a 404 response.
    #             raise

    # def

    # def sanitize(self, raw_chat):
    #     """ TODO: Formats the raw chat to put in the db, also filters out filler words
    #         Input: raw chat which is a list

    #         Output: clean chat which is a dict
    #     """

    #     ignore_words = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']

    #     chat = ' '.join(raw_chat)
    #     text = [word for word in chat.lower().split() if word not in ignore_words]
    #     return Counter(text)

        # cleaned_words = {}
        # for message in raw_chat:
        #     for word in message:
        #         if cleaned_words[word]:
        #             cleaned_words[word] += 1
        #         else:
        #             cleaned_words[word] = 1
        # return cleaned_words
