from rest_framework import serializers
from detoxipy_api.models import RecentMessage


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    message = serializers.HyperlinkedRelatedField(
        view_name='detoxipy_api',
        read_only=True
    )

    class Meta:
        model = RecentMessage
        fields = (
            'room',
            'content',
        )
