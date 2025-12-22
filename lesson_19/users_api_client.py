import logging
import sys

from requests import Response

from base_api_client import BaseAPIClient
from data_models.UserResponseModel import UserResponseModel

logging.basicConfig(level=logging.INFO, stream=sys.stdout)


class UsersApiClient(BaseAPIClient):

    def __init__(self, api_key):
        super().__init__(api_key)

    ENDPOINT = "/users"

    def create_user(self, data: dict) -> Response:
        response: Response = self._post(endpoint=self.ENDPOINT, data=data)
        if not response.ok: # response.status_code in 200x
            logging.error(f"Request failed, Status code:{response.status_code}\nResponse json: {response.json()}")
            raise AssertionError(f"Expected 200 OK, got {response.status_code}")
        UserResponseModel.model_validate(response.json())
        return response

    def get_user(self, user_id: int, expected_status_code: int = 200) -> Response:
        response = self._get(endpoint=self.ENDPOINT+f"/{user_id}")
        if response.status_code != expected_status_code: # response.status_code in 200x
            logging.error(f"Request failed, Status code:{response.status_code}\nResponse json: {response.json()}")
            raise AssertionError(f"Expected 200 OK, got {response.status_code}")
        if response.ok:
            UserResponseModel.model_validate(response.json())
        return response

    def update_user(self, user_id: int, user_data: dict) -> Response:
        response: Response = self._put(endpoint=self.ENDPOINT+f"/{user_id}", data=user_data)
        if not response.ok: # response.status_code in 200x
            logging.error(f"Request failed, Status code:{response.status_code}\nResponse json: {response.json()}")
            raise AssertionError(f"Expected 200 OK, got {response.status_code}")
        return response

    def delete_user(self, user_id: int) -> Response:
        response: Response = self._delete(endpoint=self.ENDPOINT+f"/{user_id}")
        if not response.ok: # response.status_code in 200x
            logging.error(f"Request failed, Status code:{response.status_code}\nResponse json: {response.json()}")
            raise AssertionError(f"Expected 200 OK, got {response.status_code}")
        return response

