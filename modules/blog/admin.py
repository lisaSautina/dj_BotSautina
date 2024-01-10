from django.contrib import admin
from .models import TelegramBot, Sendings


@admin.register(TelegramBot)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'name_user', 'course', 'group', 'phone_user', 'answer')

@admin.register(Sendings)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id_sending', 'text')

