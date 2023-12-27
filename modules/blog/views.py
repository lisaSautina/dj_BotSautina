

from .models import TelegramBot

from rest_framework import generics
from modules.blog.models import TelegramBot
from .serializers import TelegramMessageSerializer

class TelegramMessageList(generics.ListCreateAPIView):
    queryset = TelegramBot.objects.all()
    serializer_class = TelegramMessageSerializer

