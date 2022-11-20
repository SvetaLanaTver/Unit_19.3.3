import requests
import json


def test_create_users_array():
    # создание списка пользователей с заданным входным массивом
    input_users = json.dumps([
        {
        "id": 15,
        "username": "покупатель",
        "firstName": "Сергей",
        "lastName": "Петров",
        "email": "aa@aa.ru",
        "password": "1234",
        "phone": "string",
        "userStatus": 0
        },
        {
        "id": 16,
        "username": "покупатель",
        "firstName": "Игорь",
        "lastName": "Сорокин",
        "email": "bb@bb.ry",
        "password": "4321",
        "phone": "string",
        "userStatus": 0
        }
    ])

    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    url = 'https://petstore.swagger.io/v2/user/createWithArray'
    res = requests.post(f'{url}', headers=headers, data= input_users)

    print('\nCreating list of users with given input arrey')
    print('Код=', res.status_code)
    print(res.json())


def test_create_users_list():
    # создание списка пользователей с заданным входным списком
    input_users = json.dumps([
        {
        "id": 16,
        "username": "покупатель",
        "firstName": "Игорь",
        "lastName": "Сорокин",
        "email": "bb@bb.ry",
        "password": "4321",
        "phone": "string",
        "userStatus": 0
        },
        {
        "id": 15,
        "username": "покупатель",
        "firstName": "Сергей",
        "lastName": "Петров",
        "email": "aa@aa.ru",
        "password": "1234",
        "phone": "string",
        "userStatus": 0
        }
    ])

    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    url = 'https://petstore.swagger.io/v2/user/createWithList'
    res = requests.post(f'{url}', headers=headers, data=input_users)

    print('\nCreating list of users with given input list')
    print('Код=', res.status_code)
    print(res.json())


def test_create_user():
    # создание пользователя
    input_user = {
        "id": 14,
        "username": "Nikola_buyer",
        "firstName": "Nikola",
        "lastName": "Николаев",
        "email": "cc@cc.ru",
        "password": "0000",
        "phone": "string",
        "userStatus": 0
        }

    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    url = 'https://petstore.swagger.io/v2/user'
    res = requests.post(f'{url}', headers=headers, data=json.dumps(input_user))

    print('\nCreate user: '+input_user['username'])
    print('Код=', res.status_code)
    print(res.json())


# обновление существующего пользователя
def test_update_user():
    input_user_new = {
            "id": 14,
            "username": "Kolja_buyer",
            "firstName": "Kolja",
            "lastName": "Николаев",
            "email": "cc@cc.ru",
            "password": "0000",
            "phone": "string",
            "userStatus": 0
        }

    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    url = 'https://petstore.swagger.io/v2/user/Nikola'
    res = requests.put(f'{url}', headers=headers, data=json.dumps(input_user_new))
    result = ''
    try:
        result = res.json()
    except:
        result = res.text

    print('\nUpdate user: '+input_user_new['username'])
    print('Код=', res.status_code)
    print(result)


# получить пользователя по его имени
def test_get_user():
    headers = {'accept': 'application/json'}
    url = 'https://petstore.swagger.io/v2/user/Kolja_buyer'
    res = requests.get(f'{url}', headers=headers)

    print('\nGet user by user name')
    print('Код=', res.status_code)
    if res.status_code == 200:
        print('Пользователь найден')
    elif res.status_code == 400:
        print('Имя некорректное')
    elif res.status_code == 404:
        print('Пользователь не найден')
    print(res.json())


# регистрация пользователя
def test_log_user():
    headers = {'accept': 'application/json'}
    url = 'https://petstore.swagger.io/v2/user/login?username=Kolja_buyer&password=0000'
    res = requests.get(f'{url}', headers=headers)

    print('\nLogs user into the system')
    print('Код=', res.status_code)
    if res.status_code == 200:
        print('Пользователь зарегистрирован')
    elif res.status_code == 400:
        print('Некорректные логин или пароль')
    print(res.json())


# завершение текущего сеанса пользователя
def test_log_oot():
    headers = {'accept': 'application/json'}
    url = 'https://petstore.swagger.io/v2/user/logout'
    res = requests.get(f'{url}', headers=headers)
    print('\nLogs out current logged in user session')
    print('Код=', res.status_code)
    print(res.json())



# удаление пользователя
def test_deletes_user():
    headers = {'accept': 'application/json'}
    url = 'https://petstore.swagger.io/v2/user/Kolja_buyer'
    res = requests.delete(f'{url}', headers=headers)

    print('\nDelete user')
    print('Код=', res.status_code)
    if res.status_code == 200:
        print('Пользователь удален')
    elif res.status_code == 400:
        print('Имя некорректное')
    elif res.status_code == 404:
        print('Пользователь не найден')
    print(res.json())
