import os

from dotenv import load_dotenv

from fixtures.sausedemo import home_page
from lesson_29.page_objects.home_page.HomePage import HomePage
from lesson_29.page_objects.login_page.LoginPage import LoginPage
from lesson_29.page_objects.product_page.ProductPage import ProductPage

load_dotenv()

class TestSauseDemo:

    def test_login_is_successful(self, login_page: LoginPage):
        login_page.do_login(username=os.getenv("STANDARD_USERNAME"), password=os.getenv("STANDARD_USERPW"))
        home_page = HomePage(login_page.page)
        assert home_page.is_logged_in() is True , f"Login failed with username: {os.getenv('STANDARD_USERNAME')} and password: {os.getenv('STANDARD_USERPW')[:3]}****"

    def test_login_with_wrong_creds(self, login_page: LoginPage):
        login_page.do_login(username=os.getenv("STANDARD_USERNAME"), password=os.getenv("STANDARD_USERPW")+"000")
        home_page = HomePage(login_page.page)
        assert not home_page.is_logged_in(), f"Login NOT failed with username: {os.getenv('STANDARD_USERNAME')} and password: {os.getenv("STANDARD_USERPW")+"000"}"

    def test_select_product(self, home_page: HomePage):
        home_page.click_on_product(place=4)
        product_page = ProductPage(home_page.page)
        product_page.is_page_opened()
