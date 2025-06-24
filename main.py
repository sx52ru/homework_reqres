import pytest
import requests
import json

#class TestLogin:

def test_login():
    data = {
        "email": "lindsay.ferguson@reqres.in",
        "password": "32167nwcpadme"
    }
    response = requests.post("https://reqres.in/api/login", json=json.dumps(data))
    reqres_response = response.json()
    print(reqres_response)

