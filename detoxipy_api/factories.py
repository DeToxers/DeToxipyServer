import factory
from .models import ChatText


class ChatTextFactory(factory.django.DjangoModelFactory):
    """Create a test ChatText for writing tests."""
    class Meta:
        model = ChatText
    room_id = 689
    content = 'chat'
    count = 93
