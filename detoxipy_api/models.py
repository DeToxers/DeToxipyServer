from django.db import models


class ChatText(models.Model):
    """ A model with room_id, content, and count attributes from Twitch
    """
    room_id = models.IntegerField()
    content = models.TextField()
    count = models.IntegerField()

    def __str__(self):
        return f'{self.room_id} : {self.content} " {self.count}'
