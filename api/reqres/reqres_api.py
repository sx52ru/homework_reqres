
"""Класс-коннектор к тестируемому API"""
import allure


class Reqres_Api(Api):
    """URL"""
    _URL = "https://reqres.in"

    """Endpoint"""
    _ENDPOINT = "/api/users"

@allure.step('Обращение к create')
def reqres_create(self, param_request_body: RequestCreateUserModel):
    return self.post(url=self._URL, endpoint=self._ENDPOINT, json_body=param_request_body.to_dict())