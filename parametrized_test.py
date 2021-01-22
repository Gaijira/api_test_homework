import pytest
import requests


def test_check_server_status(url, status_code):
    r = requests.get(url)
    assert r.status_code == status_code
