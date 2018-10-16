from rest_framework import serializers
from detoxipy_api.models import Message


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    message = serializers.HyperlinkedRelatedField(
        view_name='detoxipy_api',
        read_only=True
    )

    class Meta:
        model = Message
        fields = (
            'room',
            'content',
        )
