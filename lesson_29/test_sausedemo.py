import os
from random import randint

from dotenv import load_dotenv

from fixtures.sausedemo import home_page
from lesson_29.page_objects.cart_page.cart_page import CartPage
from lesson_29.page_objects.home_page.HomePage import HomePage
from lesson_29.page_objects.login_page.LoginPage import LoginPage
from lesson_29.page_objects.product_page.ProductPage import ProductPage

load_dotenv()

class TestSauseDemo:

    def test_login_is_successful(self, login_page: LoginPage):
        home_page: HomePage = login_page.do_login(username=os.getenv("STANDARD_USERNAME"), password=os.getenv("STANDARD_USERPW"))
        assert home_page.is_logged_in() is True , f"Login failed with username: {os.getenv('STANDARD_USERNAME')} and password: {os.getenv('STANDARD_USERPW')[:3]}****"

    def test_login_with_wrong_creds(self, login_page: LoginPage):
        home_page: HomePage = login_page.do_login(username=os.getenv("STANDARD_USERNAME"), password=os.getenv("STANDARD_USERPW")+"000")
        assert not home_page.is_logged_in(), f"Login NOT failed with username: {os.getenv('STANDARD_USERNAME')} and password: {os.getenv("STANDARD_USERPW")+"000"}"

    def test_select_product(self, home_page: HomePage):
        product_page: ProductPage = home_page.click_on_product(place=4)
        product_page.is_page_opened()

    def test_add_random_product_to_cart(self, home_page: HomePage):
        product_page: ProductPage = home_page.click_on_product(place=randint(1, 6))
        product_page.add_to_cart()
        actual_count = product_page.cart_form.get_cart_counter()
        assert actual_count == 1, f"Product was added to cart but cart counter is not 1, but actually {actual_count}"

    def test_several_products_add_to_cart(self, home_page: HomePage):
        for place in range(1, 7):
            home_page.click_add_to_cart_product(place=place)
        cart_page: CartPage = home_page.cart_form.open_cart()
        assert cart_page.get_items_in_cart() == 6, f"Cart contains {cart_page.get_items_in_cart()} items, but should be 6"
