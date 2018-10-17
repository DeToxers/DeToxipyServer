from rest_framework import serializers
# from detoxipy_api.models import RecentMessage
from .models import Session


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        fields = ('id', 'message', 'total', 'room_id')

        def create(self, validated_data):
            message = super().create({
                'message': validated_data['message'],
                'total': validated_data['total'],
                'room_id': validated_data['room_id']
                # 'weight': validated_data['weight'],
                # 'time_updated': validated_data['time_updated'],
            })

            message.save()
            return message


class ChatBotSerializer(serializers.ModelSerializer):
    """ Takes in the raw ChatBot text, returns the wanted data
    """
    class Meta:
        model = Session
        fields = ('id', 'message', 'total')


# class CommentSerializer(serializers.Serializer):
#     """
#     """
#     # room_id = models.IntegerField(max_length=180, default='Untitled')
#     message = serializers.CharField(max_length=48)
#     total = serializers.IntegerField()
#     weight = serializers.FloatField()
#     time_updated = serializers.DateTimeField()
