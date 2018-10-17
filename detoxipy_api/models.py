from django.db import models


class Session(models.Model):
    """ All current sessions store their words here.
    """
    room_id = models.IntegerField(max_length=180)
    message = models.CharField(max_length=48)
    total = models.IntegerField()
    weight = models.FloatField()
    time_updated = models.DateField(auto_now=True)

    def __repr__(self):
        return f'<Word: {self.message} | {self.total} | {self.weight} >'

    def __str__(self):
        return f'{self.message} : {self.weight}'


class RecentMessage(models.Model):
    room = models.IntegerField(max_length=180)
    content = models.CharField(max_length=512, default='Untitled')
    count = models.IntegerField()
    time_updated = models.DateField(auto_now_add=True)

    def __repr__(self):
        return f'<Room: {self.room} | <Content: {self.content}>'

    def __str__(self):
        return f'{self.room} | {self.content}'


class SessionMessage(models.Model):
    room = models.IntegerField(max_length=180)
    content = models.CharField(max_length=512, default='Untitled')
    count = models.IntegerField()

class Main(models.Model):
    """ This is our long term storage for data visualization for streamers
    """
    room_id = models.IntegerField(max_length=180, default='Untitled')
    message = models.CharField(max_length=48)
    total = models.IntegerField()
    time_updated = models.DateField(auto_now=True)

    def __repr__(self):
        return f'<Main | {self.message} | {self.total}>'

    def __str__(self):
        return f'{self.message} : {self.total}'
