
import os
import requests
def send_telegram(bot_message):

    bot_token = os.environ.get("bot_token")
    bot_chatID = os.environ.get("bot_chatID")
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=HTML&text=' + bot_message

    response = requests.get(send_text)