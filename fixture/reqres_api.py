import pytest
from api.reqres.reqres_api import Reqres_Api

@pytest.fixture(scope="function")
def reqres_api() -> Reqres_Api:
    """Коннект к Reqres API"""
    return Reqres_Api()
