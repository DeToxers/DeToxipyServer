from django.db import models


class Room(models.Model):
    room_id = models.IntegerField(max_length=180, default='Untitled')
    time_started = models.DateField(auto_now_add=True)

    time_ended = models.DateField(nullable=True)

    def __repr__(self):
        return f'<Room ID: {self.room_id}>'

    def __str__(self):
        return f'{self.room_id}'


class RecentMessage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    content = models.CharField(max_length=512, default='Untitled')
    count = models.IntegerField()
    time_uploaded = models.DateField(auto_now_add=True)

    def __repr__(self):
        return f'<Room: {self.room} | <Content: {self.content}>'

    def __str__(self):
        return f'{self.room} | {self.content}'
