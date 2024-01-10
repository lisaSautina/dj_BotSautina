from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import TelegramBot
from rest_framework import generics

from .serializers import TelegramMessageSerializer
from django.shortcuts import render
import requests

class TelegramMessageList(generics.ListCreateAPIView):
    queryset = TelegramBot.objects.all()
    serializer_class = TelegramMessageSerializer

def broadcast_message_view(request):
    return render(request, 'broadcast.html')


@csrf_exempt 
def send_broadcast_message(request):
    if request.method == 'POST':                         
        message = request.POST.get('message', '')  # получаем сообщение
        
        subscribers = TelegramBot.objects.filter(answer='да')
        bot_token = '6895766351:AAHs8k5kgSpLArv0mo_vX7lWbSn25GKmttA' 

        for i in subscribers:
            url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
            data = {'chat_id': i.id_user, 'text': message}
            requests.post(url, data=data)

        return HttpResponse('Сообщение отправлено.')
    else:
        return HttpResponse('Ошибка', status=400)
