from django.contrib import admin
from .models import Session


# Register your models here.


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'message', 'total', 'weight', 'time_updated')

