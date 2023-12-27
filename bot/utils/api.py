import requests
import json

DATABASE_URL = 'http://localhost:8000/api/v1'

def create_user(id_user, name_user, phone_user, course, group):
    url = f"{DATABASE_URL}/bot-users"
    response = requests.get(url=url).text
    data = json.loads(response)
    user_exist = False
    for i in data: 
        if i['id_user'] == str(id_user):
            user_exist = True
            break
    if user_exist == False:
        requests.post(url=url, data={'id_user':id_user, 'name_user':name_user, 'phone_user':phone_user, 'course': course, 'group': group})
        return 'Вы зарегистрированы'
    else:
        return 'Такой пользователь уже есть'
    


