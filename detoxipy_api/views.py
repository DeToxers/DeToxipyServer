from rest_framework import generics
import json
from .serializers import ChatTextSerializer
from .models import ChatText
from django_rest_framework import JsonResponse

from rest_framework.response import Response


class MessagePostApiView(generics.CreateAPIView):
    """ This is what handles when the ChatBot sends up text
    """
    model = ChatText
    serializer_class = ChatTextSerializer

    def get(request):
        """
        Grabs all messages, serializes them and returns them as JSON
        """
        if request == 'GET':
            messages = ChatText.objects.all()
            serializer = ChatTextSerializer(messages, many=True)
            return JsonResponse(serializer.data, safe=False)

    def post(self, *args, **kwargs):
        """
            This posts all chat data recieved to the database.

            [Input]

                An HTTP Request that contains JSON of our chat data

            [Output]

                HTTP Response code. Returns 404(actually a 500). If it successful returns status code 201
        """
        # get the chat data in a form we can use
        data = json.loads(kwargs['vals'])
        room_id = kwargs['room_id']

        # put those in the db
        for item in data:
            for k, v in item.items():
                chat = ChatText()
                chat.room_id = room_id
                chat.content = k
                chat.count = v
                chat.save()
        return generics.response(status=201)
