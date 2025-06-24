import pytest
import requests
import json

@pytest.fixture(scope="function", autouse=True)

def register_user():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
           }
    response = requests.post("https://reqres.in/api/register", json=json.dumps(data))
    reqres_response = response.json()
    print(reqres_response)