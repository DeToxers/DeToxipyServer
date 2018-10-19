from rest_framework import serializers
from .models import ChatText


class ChatBotSerializer(serializers.ModelSerializer):
    """ Takes in the raw ChatBot text, returns the wanted data
    """
    room_id = serializers.IntegerField()
    json_chat = serializers.CharField()

    class Meta:
        model = ChatText
        fields = ('room_id', 'json_chat')
