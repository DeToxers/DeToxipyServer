from django.contrib import admin
from .models import ChatText


# Register your models here.


# @admin.register(Session)
# class SessionAdmin(admin.ModelAdmin):
#     list_display = ('room_id', 'message', 'total', 'weight', 'time_updated')

@admin.register(ChatText)
class ChatTextAdmin(admin.ModelAdmin):
    """ Registers the ChatText Model
    """
    list_display = ('room_id', 'content', 'count')
