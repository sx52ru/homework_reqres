import requests
import json
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

def test_login_with_registered_user(registered_user):
    """Проверка входа с зарегистрированным пользователем"""
    login_response = requests.post(
        f'{TEST_URL}login',
        data=json.dumps({'email': registered_user['email'], 'password': registered_user['password']}),
        headers={'Content-Type': 'application/json', 'x-api-key': 'reqres-free-v1', 'Connection': 'keep-alive'}
    )

    assert login_response.status_code == 200
    assert 'token' in login_response.json()
