from django.db import models


class ChatText(models.Model):
    """
    """
    room_id = models.IntegerField()
    json_chat = models.TextField()

    def __str__(self):
        return f'{self.room_id} : {self.json_chat}'

