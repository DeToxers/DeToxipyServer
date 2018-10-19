from django.contrib import admin
from .models import Session, ChatText


# Register your models here.


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'message', 'total', 'weight', 'time_updated')

@admin.register(ChatText)
class ChatTextAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'json_chat')
