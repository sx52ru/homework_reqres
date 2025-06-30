from http.client import responses

import allure
import requests
from jsonschema.validators import validate
from helper.load import load_json_schema

from helper.logger import log

class Api:
    """Основной класс"""
    _HEADERS = {'Content-type':'application/json; charset=utf-8', 'x-api-key': 'reqres-free-v1', 'Connection': 'keep-alive'}
    _TIMEOUT = 10
    base_url = {}

    def __init__(self):
        self.response = None

    @allure.step('Отправить POST-запрос')
    def post(self, url: str, endpoint: str, params: dict = None, json_body: dict = None):
        with allure.step(f'POST-запрос на url: {url}{endpoint} \nтело запроса: \n{json_body}'):
            self.response = requests.post(url=f'{url}{endpoint}', headers=self._HEADERS, params=params, json=json_body, timeout=self._TIMEOUT)
            log(response=self.response, request_body=json_body)
            return self

    @allure.step('Статус-код равен {expected code}')
    def status_code_should_be(self, expected_code: int):
        """Проверка статус-код ответа actual_code на соответствие expected_code"""
        actual_code = self.response.status_code
        assert expected_code == actual_code, f'\nОжидаемый результат: {expected_code}' \
                                             f'\nФактический результат {actual_code}'
        return self

    @allure.step('OP: схема ответа json валидна')
    def json_schema_should_be_valid(self, path_json_schema: str, name_json_schema: str = 'schema'):
        """Проверка полученного ответа на соответствие json-схеме"""
        json_schema = load_json_schema(path_json_schema, name_json_schema)
        validate(self.response.json())
        return self

    @allure.step("OP: Объекты равны")
    def objects_should_be(self, expected_object, actual_object):
        """Сравнение двух объектов"""
        assert expected_object == actual_object, f'\nОжидаемый объект {expected_object}' \
                                                 f'\nФактический объект: {actual_object}'
        return self

    @allure.step("OP: в поле ответа содержится искомое значение")
    def have_value_in_response_parameter(self, keys: list, value: str):
        """Сравниваем значение необходимого параметра"""
        payload = self.get_payload(keys)
        assert value == payload, f'\nОжидаемый результат: {value}' \
                                 f'\nФактический результат: {payload}'
        return self

    def get_payload(self, keys: list):
        """Получаем результат (payload) переходя по ключам и возвращаем его"""
        response = self.response.json()
        payload = self.json_parser.find_json_vertex(response, keys)
        return payload

    






