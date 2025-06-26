import pytest
import requests
import json


def test_login_with_registered_user(registered_user):
    """Проверка входа с зарегистрированным пользователем"""
    login_response = requests.post(
        'https://reqres.in/api/login',
        data=json.dumps({'email': registered_user['email'], 'password': registered_user['password']}),
        headers={'Content-Type': 'application/json', 'x-api-key': 'reqres-free-v1', 'Connection': 'keep-alive'}
    )

    assert login_response.status_code == 200
    assert 'token' in login_response.json()
