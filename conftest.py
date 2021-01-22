import pytest


def pytest_addoption(parser):
    parser.addoption('--url',
                     default='https://ya.ru',
                     type=str,
                     help='Inserts a given url, default - ya.ru'
                     )
    parser.addoption('--status_code',
                     default=200,
                     action='store',
                     type=int,
                     help='Inserts a given status code, default - 200'
                     )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")
