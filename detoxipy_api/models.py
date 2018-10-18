from django.db import models


class ChatText(models.Model):
    """
    """
    room_id = models.IntegerField()
    content = models.TextField()
    count = models.IntegerField()

    def __str__(self):
        return f'{self.room_id} : {self.content} " {self.count}'
