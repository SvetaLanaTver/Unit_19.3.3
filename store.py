import requests
import json


# размещение заказа на покупку питомца
def test_place_an_order():
    # создание нового питомца
    input_pet = {
        "id": 22222,
        "category": {
            "id": 111122,
            "name": "Nona"
        },
        "name": "cat",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 122112,
                "name": "cat"
            }
        ],
        "status": "placed"
    }

    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    url = 'https://petstore.swagger.io/v2/pet'
    res = requests.post(f'{url}', headers=headers, data=json.dumps(input_pet))

    if res.status_code == 200:
        print('\nAdded a new to the store')
        data = {
            "id": 22222,
            "petId": 2222,
            "quantity": 1,
            "shipDate": "2022-11-19T13:52:06.549Z",
            "status": "placed",
            "complete": True
        }
        headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
        url = 'https://petstore.swagger.io/v2/store/order'
        res = requests.post(f'{url}', headers=headers, data=json.dumps(data))
        print('\nPlace an order for a pet')
        print('Код=', res.status_code)
        print(res.json())


# поиск заказа на покупку по идентификатору
def test_find_order():
    headers = {'accept': 'application/json'}
    url = 'https://petstore.swagger.io/v2/store/order/1'
    res = requests.get(f'{url}', headers=headers)

    print('\nFind purchase order by ID')
    print('Код=', res.status_code)
    if res.status_code == 200:
        print('Заказ найден')
    elif res.status_code == 400:
        print('ID некорректный')
    elif res.status_code == 404:
        print('Заказ не найден')
    print(res.json())


# удаление заказа на покупку
def test_deletes_order():
    headers = {'accept': 'application/json'}
    url = 'https://petstore.swagger.io/v2/store/order/1'
    res = requests.delete(f'{url}', headers=headers)

    print('\nDelete purchase order by ID')
    print('Код=', res.status_code)
    if res.status_code == 200:
        print('Заказ удален')
    elif res.status_code == 400:
        print('ID некорректный')
    elif res.status_code == 404:
        print('Заказ не найден')

    result = ''
    try:
        result = res.json()
    except:
        result = res.text

    print(result)


# инвентаризация животных по статусу
def test_inventory():
    headers = {'accept': 'application/json'}
    url = 'https://petstore.swagger.io/v2/store/inventory'
    res = requests.get(f'{url}', headers=headers)
    print('\nReturns pet inventories by status')
    print('Код=', res.status_code)
    print(res.json())


# удаление питомца
def test_deletes():
    petID = 22222
    headers = {'accept': 'application/json', 'api_key': 'special-key'}
    url = 'https://petstore.swagger.io/v2/pet/22222'
    res = requests.delete(f'{url}', headers=headers)

    print('\nDeletes a pet')
    print('Код=', res.status_code)
    if res.status_code == 200:
        print('Питомец удален')
    elif res.status_code == 400:
        print('ID некорректный')
    elif res.status_code == 404:
        print('Питомец не найден')
    print(res)
