import logging

from requests import Response

from base_api_client import BaseAPIClient


class UsersApiClient(BaseAPIClient):

    def __init__(self, api_key):
        super().__init__(api_key)

    ENDPOINT = "/users"

    def create_user(self, data: dict) -> Response:
        print(f"Sending request to {self.ENDPOINT}, data: {data}")
        response = self._post(endpoint=self.BASE_URL+self.ENDPOINT, data=data)
        if not response.ok:
            logging.info(f"Response: {response.json()}")
            raise AssertionError(f"Request failed: {response.json()}")

    def get_user(self, user_id: int) -> Response:
        response = self._get(endpoint=self.ENDPOINT+f"/{user_id}")
        if not response.ok:
            raise AssertionError(f"Request failed: {response.text}")


user_api_client = UsersApiClient('819e69004d2ea659faf886ece1355d4994f2b390ba9b76253a01dfbe3d02980b')

print(user_api_client.get_user(user_id=8303219))