from django.contrib import admin
from .models import SessionCache


# Register your models here.


@admin.register(SessionCache)
class SessionCacheAdmin(admin.ModelAdmin):
    list_display = ('top_five', 'room_id')
