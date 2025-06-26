import pytest
import requests
import json


@pytest.fixture
def registered_user():
    """Фикстура для регистрации нового пользователя"""
    # Данные для регистрации
    registration_data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    # Отправка POST запроса на регистрацию
    response = requests.post(
        'https://reqres.in/api/register',
        data=json.dumps(registration_data),
        headers={'Content-Type': 'application/json', 'x-api-key': 'reqres-free-v1', 'Connection': 'keep-alive'}
    )

    # Проверка статуса регистрации
    assert response.status_code == 200, "Регистрация не прошла успешно"

    # Получение токена из ответа
    registration_token = response.json()['token']

    # Создание словаря с данными зарегистрированного пользователя
    user_data = {
        'token': registration_token,
        'email': registration_data['email'],
        'password': registration_data['password']
    }

    yield user_data  # Возврат данных пользователя

    # Очистка - удаление пользователя после теста
    #requests.delete(
    #    f'https://reqres.in/api/users?token={registration_token}',
    #    headers={'Content-Type': 'application/json'}
    #)