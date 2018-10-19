from rest_framework import serializers
from .models import ChatText


class ChatTextSerializer(serializers.ModelSerializer):
    """ Takes in the raw ChatBot text, returns the wanted data
    """
    room_id = serializers.IntegerField()
    content = serializers.CharField()
    count = serializers.IntegerField()

    class Meta:
        model = ChatText
        fields = ('room_id', 'content', 'count')
