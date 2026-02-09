import os

import allure
from playwright.sync_api import Page, Locator, expect
from dotenv import load_dotenv

from lesson_29.page_objects.home_page.HomePage import HomePage

load_dotenv()

class LoginPage:
    # user_name_input = "#user-name"
    # password_input = "#password"
    # login_button = "#login-button"

    def __init__(self, page: Page):
        self.page = page
        self.url = os.getenv("SAUSEDEMO_BASE_URL")

    @property
    def username_field(self) -> Locator:
        return self.page.locator("#user-name")

    @property
    def password_field(self) -> Locator:
        return self.page.locator("#password")

    @property
    def login_button(self) -> Locator:
        return self.page.locator("#login-button")

    def type_username(self, username: str):
        self.username_field.type(username)
        return self

    def type_password(self, password: str):
        self.password_field.type(password)
        return self

    def click_login_button(self):
        self.login_button.click()
        return self

    @allure.step("Open Sause Demo Store")
    def open(self) -> None:
        self.page.goto(url=self.url)

    @allure.step("Login to Sause Demo Store")
    def do_login(self, username: str, password: str) -> HomePage:
        self.username_field.type(username, delay=100)
        self.password_field.type(password, delay=100)
        self.login_button.click()
        return HomePage(self.page)


