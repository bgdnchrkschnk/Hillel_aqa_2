import logging
import os

import faker
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
        assert response.json().get("id") is not None

    def test_getting_user(self):
        test_user_data: dict = get_create_user_request()
        response: Response = self.user_api_client.create_user(test_user_data)
        user_id = response.json().get("id")

        # GET USER
        response: Response = self.user_api_client.get_user(user_id=user_id)
        logging.info(f"Test user data: {test_user_data}")
        logging.info(f"User from server by user_id - {response.json()}")
        assert test_user_data.items() <= response.json().items()

    def test_update_user(self):
        # create a new user
        test_user_data: dict = get_create_user_request()
        response: Response = self.user_api_client.create_user(test_user_data)
        user_id = response.json().get("id")

        user_data_to_update: dict = {
            "name": "Updated name",
            "email": faker.Faker().email(),
        }

        # update user by id
        response: Response = self.user_api_client.update_user(user_id=user_id, user_data=user_data_to_update)

        # get user and assert data is updated successfully
        response: Response = self.user_api_client.get_user(user_id=user_id)
        assert response.json().get("name") == user_data_to_update["name"]
        assert response.json().get("email") == user_data_to_update["email"]


    def test_user_delete(self):
        # create a new user
        test_user_data: dict = get_create_user_request()
        response: Response = self.user_api_client.create_user(test_user_data)
        user_id = response.json().get("id")

        # delete user by user id
        response: Response = self.user_api_client.delete_user(user_id=user_id)

        # get_user assert
        response: Response = self.user_api_client.get_user(user_id=user_id, expected_status_code=404)
        assert response.json().get("message") == "Resource not found"




# response.status_code
# response.headers
# response.text -> str
# response.json() # JSON string - json.loads(response.text) -> python dict
# response.cookies
# response.url
# response.content # file - bytes
# response.ok # bool(status_code) in 200x