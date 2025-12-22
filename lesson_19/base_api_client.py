import logging
import os
from dotenv import load_dotenv
import requests
from requests import Response

load_dotenv()


class BaseAPIClient:

    BASE_URL = os.getenv("BASE_URL")

    def __init__(self, api_key):
        self.__api_key = api_key
        self.session = requests.Session()
        self.__authentificate()

    def _headers_update(self, headers: dict) -> None:
        self.session.headers.update(headers)

    def _clear_headers(self) -> None:
        self.session.headers.clear()

    def __authentificate(self) -> None:
        headers = {
            "Authorization": f"Bearer {self.__api_key}",
            "Content-Type": "application/json"
        }
        self._headers_update(headers)

    @property
    def api_key(self) -> str: # obj.api_key ->
        return self.__api_key

    def _get(self, endpoint: str) -> Response:
        return self.session.get(url=f"{self.BASE_URL}{endpoint}", timeout=10)

    def _post(self, endpoint: str, data: dict) -> Response:
        return self.session.post(url=f"{self.BASE_URL+endpoint}", json=data, timeout=10)

    def _put(self, endpoint: str, data: dict) -> Response:
        return self.session.put(url=f"{self.BASE_URL+endpoint}", json=data, timeout=10)

    def _delete(self, endpoint: str) -> Response:
        return self.session.delete(url=f"{self.BASE_URL+endpoint}", timeout=10)
