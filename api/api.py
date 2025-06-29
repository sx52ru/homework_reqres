import allure
import requests
from helper.logger import log

class Api:
    '''Основной класс'''
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

