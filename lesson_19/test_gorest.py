import os

from dotenv import load_dotenv
from requests import Response

from data_provider import get_create_user_request
import requests
from users_api_client import UsersApiClient
load_dotenv()


class TestGorestAPI:
    user_api_client = UsersApiClient(api_key=os.getenv("API_TOKEN"))

    def test_user_creation(self):
        test_user_data: dict = get_create_user_request()
        response: Response = self.user_api_client.create_user(test_user_data)
        response_json = response.json()
        assert response.json().get("id") is not None

    def test_getting_user(self):
        test_user_data: dict = get_create_user_request()
        response: Response = self.user_api_client.create_user(test_user_data)
        user_id = response.json().get("id")

        # GET USER
        response: Response = self.user_api_client.get_user(user_id=user_id)
        assert test_user_data.items() <= response.json().items()







# response.status_code
# response.headers
# response.text -> str
# response.json() # JSON string - json.loads(response.text) -> python dict
# response.cookies
# response.url
# response.content # file - bytes
# response.ok # bool(status_code) in 200x