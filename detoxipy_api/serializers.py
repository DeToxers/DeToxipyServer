from rest_framework import serializers
from .models import ChatText


class ChatTextSerializer(serializers.ModelSerializer):
    """ Takes in the raw ChatBot text, returns the wanted data
    """
    room_id = serializers.IntegerField()
    content = serializers.TextField()
    count = serializers.IntegerField()

    class Meta:
        model = ChatText
        fields = ('room_id', 'content', 'count')


# class CommentSerializer(serializers.Serializer):
#     """
#     """
#     # room_id = models.IntegerField(max_length=180, default='Untitled')
#     message = serializers.CharField(max_length=48)
#     total = serializers.IntegerField()
#     weight = serializers.FloatField()
#     time_updated = serializers.DateTimeField()
