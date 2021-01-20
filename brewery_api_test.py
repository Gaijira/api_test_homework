import pytest
import requests


# Test for incorrect request lead to 404
def test_invalid_status():
    r = requests.get('https://api.openbrewerydb.org/breweries1')
    assert r.status_code == 404


# Тест на выдачу валидного ответа по заданному городу
def test_city_state_search():
    r = requests.get('https://api.openbrewerydb.org/breweries?by_city=New York')
    json = r.json()
    for el in json:
        assert el["city"] == "New York" and r.status_code == 200


# Тест на выдачу заданного кол-ва элементов
@pytest.mark.parametrize('pages', [25, 35, 45])
def test_per_page(pages):
    r = requests.get(f'https://api.openbrewerydb.org/breweries?per_page={pages}')
    json = r.json()
    assert len(json) == pages and r.status_code == 200


# Тест на выдачу значений отсортированнх по возрастанию
@pytest.mark.parametrize('param', ['+id', '-id'])
def test_sorting_by_id_ascending(param):
    r = requests.get(f'https://api.openbrewerydb.org/breweries?sort={param}')
    json = r.json()
    ids = []
    for el in json:
        ids.append(el.pop('id'))
    if param == '+id':
        assert ids == sorted(ids) and r.status_code == 200
    else:
        assert ids == sorted(ids, reverse=True) and r.status_code == 200


@pytest.mark.parametrize('brewery_type', ['micro', 'nano', 'regional'])
def test_search_by_type(brewery_type):
    r = requests.get(f'https://api.openbrewerydb.org/breweries?by_type={brewery_type}')
    json = r.json()
    for el in json:
        assert type in el['brewery_type'] and r.status_code == 200
