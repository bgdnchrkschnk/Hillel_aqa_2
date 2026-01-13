import pytest

from lesson_24.base_qauto_api_client import BaseQAutoApiClient

@pytest.fixture(scope="session")
def api_client():
    api_client = BaseQAutoApiClient()
    yield api_client
    api_client.session.close()
    del api_client