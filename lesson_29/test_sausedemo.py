import os

from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

from lesson_29.page_objects.home_page.HomePage import HomePage
from lesson_29.page_objects.login_page.LoginPage import LoginPage
from lesson_29.page_objects.product_page.ProductPage import ProductPage

load_dotenv()

class TestSauseDemo:

    def test_login_is_successful(self, login_page: LoginPage, home_page_unlogged: HomePage):
        login_page.do_login(username=os.getenv("STANDARD_USERNAME"), password=os.getenv("STANDARD_USERPW"))
        assert home_page_unlogged.is_logged_in() is True , f"Login failed with username: {os.getenv('STANDARD_USERNAME')} and password: {os.getenv('STANDARD_USERPW')[:3]}****"

    def test_login_with_wrong_creds(self, login_page: LoginPage, home_page_unlogged: HomePage):
        login_page.do_login(username=os.getenv("STANDARD_USERNAME"), password=os.getenv("STANDARD_USERPW")+"000")
        assert not home_page_unlogged.is_logged_in(), f"Login NOT failed with username: {os.getenv('STANDARD_USERNAME')} and password: {os.getenv("STANDARD_USERPW")+"000"}"

    def test_select_product(self, home_page_with_login: HomePage):
        home_page_with_login.click_on_product(place=4)
        product_page = ProductPage(home_page_with_login.page)
        product_page.is_page_opened()
