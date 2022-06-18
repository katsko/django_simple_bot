from django.contrib import admin
from .models import Msg


@admin.register(Msg)
class MsgAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
