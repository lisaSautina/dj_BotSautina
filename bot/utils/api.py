from aiogram import Bot

import requests
import json

DATABASE_URL = 'http://localhost:8000/api/v1/'

async def create_user(id_user, name_user, course, group, phone_user, answer):
    try:
        # GET запрос для проверки существования пользователя
        response = requests.get(f'{DATABASE_URL}message/')
        response.raise_for_status()  # Проверка успешности GET-запроса
        # Проверка, что ответ сервера не пуст и является JSON
        if response.text:
            data = response.json()
            
            # Проверка существования пользователя по id_user
            user_exist = any(user['id_user'] == id_user for user in data)

            if not user_exist:
                # POST запрос для создания пользователя
                payload = {
                    'id_user': id_user,
                    'name_user': name_user,
                    'course': course,
                    'group': group,
                    'phone_user': phone_user,
                    'answer': answer
                }

                response = requests.post(f'{DATABASE_URL}message/', json=payload)
                response.raise_for_status()  # Проверка успешности POST-запроса

                return 'Вы зарегистрированы'
            else:
                return 'Такой пользователь уже есть'
        else:
            return 'Ошибка: Пустой ответ от сервера'

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return 'все не ок'
    
# def get_text(id):
#     url_mailing = f"{DATABASE_URL}/mail-list"
#     response_mailing = requests.get(url=url_mailing)
#     data = response_mailing.json()
#     return data





    


