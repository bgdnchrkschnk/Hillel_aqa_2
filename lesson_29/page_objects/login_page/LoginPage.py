import os
from playwright.sync_api import Page, Locator, expect
from dotenv import load_dotenv
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

    def open(self):
        self.page.goto(url=self.url)

    def do_login(self, username: str, password: str):
        self.username_field.type(username, delay=100)
        self.password_field.type(password, delay=100)
        self.login_button.click()
