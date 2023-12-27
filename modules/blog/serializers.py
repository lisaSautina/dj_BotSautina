from rest_framework import serializers
from modules.blog.models import TelegramBot

class TelegramMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramBot
        fields = '__all__'