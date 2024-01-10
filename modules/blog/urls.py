from django.urls import path
from .views import TelegramMessageList
from .views import send_broadcast_message, broadcast_message_view
urlpatterns = [
    path('message/', TelegramMessageList.as_view(), name='message-bot'),
    path('send-broadcast/', send_broadcast_message, name='send_broadcast'),
    path('message1/', broadcast_message_view, name='broadcast_message'),
]