import pytest
import requests
import json

# Open json file
with open('user.json', 'r') as f:
    data = json.load(f)


# Тест на успешный put запрос
def test_put():
    put = requests.put('https://jsonplaceholder.typicode.com/users/1', data=data)
    response = put.json()
    assert response['name'] == 'Bruce Wayne' and put.status_code == 200


# Тест на успешный вывод пользователей по id
@pytest.mark.parametrize('param', [1, 2, 3, 4])
def test_get(param):
    get = requests.get(f'https://jsonplaceholder.typicode.com/users/{param}')
    response = get.json()
    assert response['id'] == param and get.status_code == 200
    print(response)


# Тест на успешный delete запрос
def test_delete():
    delete = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
    response = delete.json()
    assert delete.status_code == 200 and response == {}


# Тест на выдачу параматрезованного запроса комментариев по номеру поста
@pytest.mark.parametrize('param', [1, 2, 3, 4])
def test_parametrized_posts(param):
    get = requests.get(f'https://jsonplaceholder.typicode.com/comments?postId={param}')
    response = get.json()
    for el in response:
        assert param == el['postId'] and get.status_code == 200


# Тест на кол-во выводимых фотографий по умолчанию -5000
def test_posts_quantity():
    get = requests.get('https://jsonplaceholder.typicode.com/photos')
    response = get.json()
    assert len(response) == 5000 and get.status_code == 200
