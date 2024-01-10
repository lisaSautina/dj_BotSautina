# import requests
# import json
# import os
# from utils.api import get_text
# from aiogram import Bot
# from aiogram.types import Message
# from dotenv import load_dotenv


# load_dotenv()

# DATABASE_URL = os.getenv('DATABASE_URL')


# async def get_mailing(message: Message, bot: Bot):
#     url = f"{DATABASE_URL}/bot-users"
#     response = requests.get(url=url).text
#     data = json.loads(response)

#     msg = str(get_text(1))

#     for i in data:
#         if i["consent_mail_list"] == "Да":
#             await bot.send_message(message.from_user.id, msg)
#             break