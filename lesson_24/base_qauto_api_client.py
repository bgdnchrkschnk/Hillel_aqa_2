import json

import requests
from requests import Session, Response

from lesson_24.abstract_api_client import AbstractApiClient
from lesson_24.data_models.logout_response import LogoutResponseModel
from lesson_24.data_models.sign_in_response import SignInResponseModel
from lesson_24.data_models.sign_up_response import SignUpResponseModel
from lesson_24.data_provider.sign_up_data import get_sign_up_data
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class BaseQAutoApiClient(AbstractApiClient):

    BASE_URL = 'https://qauto.forstudy.space/api'

    def __init__(self):
        self.session: Session = requests.Session()
        self.session.headers.update({'Content-Type': 'application/json'})

    def _post(self, endpoint: str, data: dict):
        final_endpoint = f'{self.BASE_URL}/{endpoint}'
        logging.info(f'Sending POST request to {final_endpoint} with data: {data}')
        return self.session.post(final_endpoint, json=data)

    def _get(self, endpoint: str):
        final_endpoint = f'{self.BASE_URL}/{endpoint}'
        return self.session.get(final_endpoint)

    def _put(self, endpoint: str, data: dict):
        final_endpoint = f'{self.BASE_URL}/{endpoint}'
        return self.session.put(final_endpoint, json=data)

    def _delete(self, endpoint: str):
        final_endpoint = f'{self.BASE_URL}/{endpoint}'
        return self.session.delete(final_endpoint)

    def sign_up(self, sign_up_data: dict) -> Response:
        endpoint = "/auth/signup"
        response: Response = self._post(endpoint, sign_up_data)
        logging.info(f"Validation response: {response.json()}")
        SignUpResponseModel.model_validate(response.json())
        return response

    def sign_in(self, email: str, password: str) -> Response:
        endpoint = "/auth/signin"
        sign_in_data = {"email": email, "password": password}
        response = self._post(endpoint, sign_in_data)
        logging.info(f"Validation response: {response.json()}")
        SignInResponseModel.model_validate(response.json())
        return response

    def log_out(self) -> Response:
        endpoint = "/auth/logout"
        response = self._get(endpoint)
        logging.info(f"Validation response: {response.json()}")
        LogoutResponseModel.model_validate(response.json())
        return response


# if __name__ == '__main__':
#     api_client = BaseQAutoApiClient()
#     sign_up_data = get_sign_up_data()
#
#     logging.info(api_client.session.cookies.get_dict())
#
#     response = api_client.sign_up(sign_up_data=sign_up_data)
#
#     logging.info(response.headers)
#     logging.info(response.json())
#     logging.info(api_client.session.cookies.get_dict())
#
#     response = api_client.sign_in(email=sign_up_data['email'], password=sign_up_data['password'])
#
#     logging.info(response.json())
#
#     print(api_client.session.close())

