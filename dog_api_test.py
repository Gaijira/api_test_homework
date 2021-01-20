import requests
import pytest


# Тест на валидный ответ от сервера
def test_status():
    url = requests.get(f'https://dog.ceo/api/')
    assert url.status_code == 200


# Тест на успешную выдачу случайного изображения
def test_success_random():
    url = requests.get('https://dog.ceo/api/breeds/image/random')
    json = url.json()
    assert json['status'] == 'success' and url.status_code == 200


# Тест на успешную выдачу параметрезованного кол-ва случайных изображений
@pytest.mark.parametrize('number', [3, 4, 5])
def test_multiple_images(number):
    url = requests.get(f'https://dog.ceo/api/breeds/image/random/{number}')
    json = url.json()
    assert len(json['message']) == number and json['status'] == 'success' and url.status_code == 200


# Тест на успешную выдачу параметрезованных пород
@pytest.mark.parametrize('given', ['african', 'hound', 'akita'])
def test_random_breed(given):
    url = requests.get(f'https://dog.ceo/api/breed/{given}/images/random')
    json = url.json()
    assert json['status'] == 'success' and given in json['message'] and url.status_code == 200


# Тест на успешную выдачу подпород для указнной породы
def test_sub_breed():
    url = requests.get('https://dog.ceo/api/breed/hound/list')
    json = url.json()
    assert json['message'] != 0 and json['status'] == 'success' and url.status_code == 200
