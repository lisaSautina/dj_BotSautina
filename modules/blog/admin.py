from django.contrib import admin
from .models import TelegramBot


@admin.register(TelegramBot)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'name_user', 'course', 'group', 'phone_user')

