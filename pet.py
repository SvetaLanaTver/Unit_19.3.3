import requests
import json


# добавление нового питомца
def test_add_pet():
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
          "status": "available"
    }

    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    url = 'https://petstore.swagger.io/v2/pet'
    res = requests.post(f'{url}', headers=headers, data=json.dumps(input_pet))

    result = ''
    try:
        result = res.json()
    except:
        result = res.text

    print('\nAdd a new to the store')
    print('Код=', res.status_code)
    print(result)


# загрузка изображения
def test_upload_image():
    image = '7b64.jpg'
    pet_photo = {'file': (image, open(image, 'rb'), 'image/jpeg')}
    headers = {'accept': 'application/json'}
    url = 'https://petstore.swagger.io/v2/pet/22222/uploadImage'
    res = requests.post(f'{url}', headers=headers, files=pet_photo)
    print('\nUploads an image')
    print('Код=', res.status_code)
    print(res.json())


# обновление существующего питомца
def test_update():
    input_pet = {
        "id": 22222,
        "category": {
            "id": 111122,
            "name": "Нюша"
        },
        "name": "cat",
        "photoUrls": [
            "7b64.jpg"
        ],
        "tags": [
            {
                "id": 122112,
                "name": "cat"
            }
        ],
        "status": "available"
    }
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    url = 'https://petstore.swagger.io/v2/pet'
    res = requests.put(f'{url}', headers=headers, data=json.dumps(input_pet))
    result = ''
    try:
        result = res.json()
    except:
        result = res.text

    print('\nUpdate an existing pet')
    print('Код=', res.status_code)
    print(result)


# находит питомцев по статусу
def test_status():
    status = 'available'
    headers = {'accept': 'application/json'}
    url = 'https://petstore.swagger.io/v2/pet/findByStatus?status'
    res = requests.get(f'{url}={status}', headers=headers)
    print('\nFinds Pets by status')
    print('Код=', res.status_code)
    print(res.json())


# поиск питомца по идентификатору
def test_find_pet():
    headers = {'accept': 'application/json'}
    url = 'https://petstore.swagger.io/v2/pet/22222'
    res = requests.get(f'{url}', headers=headers)
    print('\nFinds Pet by ID')
    print('Код=', res.status_code)
    print(res.json())


# обновление питомца с помощью данных формы
def test_updates():
    name = "Нюнька"
    status = 'sold'
    headers = {'accept': 'application/json'}
    data = f'name={name}&status={status}'
    url = 'https://petstore.swagger.io/v2/pet/22222'
    res = requests.post(f'{url}', headers=headers, data=json.dumps(data))

    result = ''
    try:
        result = res.json()
    except:
        result = res.text

    print('\nAdd a new to the store')
    print('Код=', res.status_code)
    print(result)


# удаление питомца
def test_deletes():
    headers = {'accept': 'application/json', 'api_key': 'special-key'}
    url = 'https://petstore.swagger.io/v2/pet/22222'
    res = requests.delete(f'{url}', headers=headers)

    result = ''
    try:
        result = res.json()
    except:
        result = res.text

    print('\nDeletes a pet')
    print('Код=', res.status_code)
    print(result)
