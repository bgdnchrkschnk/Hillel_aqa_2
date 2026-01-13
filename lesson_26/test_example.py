import logging
from random import randint

import pytest
import requests

from lesson_22.db_client import DBClient
from lesson_23.user import User
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.mark.usefixtures("sound_notification")
class TestExample:

    def sum(self, x, y):
        return x + y

    @pytest.mark.parametrize("test_number", [1, 4, 6, 9])
    def test_example_randint(self, test_number, api_client):
        assert test_number % 2 == 0

        requests.get(auth=, params={"sorting_by": "price", })


    # @pytest.mark.parametrize("user": ["admin", "moderator", "vip", "regular"])
    # def login_out(self, user: User, webdriver: WebDriver, api_client):
    #     webdriver.get("https://www.test-service.com/")
    #     login_with_creds(user_object=user)
    #     webdriver.find_element_by_css_selector(".logout-btn").click()


    @pytest.mark.parametrize("x, y, expected", [
        (1, 2, 3),
        (5, 5, 10),
        (10, -5, 5)
    ])
    def test_addition(self, x, y, expected, api_client):
        logging.info(f"Testing addition of {x} and {y}")
        result = self.sum(x, y)
        assert result == expected

    def test_name_is_alex(self, request, name):
        logging.info(f"TEST NAME: {request.node.name}")
        assert name == "Alex"