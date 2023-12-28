from django.urls import path
from .views import TelegramMessageList
urlpatterns = [
    path('message/', TelegramMessageList.as_view(), name='message-bot'),
    # Добавьте другие URL, если необходимо
]