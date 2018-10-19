from django.contrib import admin
from .models import ChatText


# Register your models here.

@admin.register(ChatText)
class ChatTextAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'json_chat')
