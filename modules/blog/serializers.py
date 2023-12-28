from rest_framework import serializers
from modules.blog.models import TelegramBot

class TelegramMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramBot
        fields = ('id_user', 'name_user', 'course','group','phone_user')