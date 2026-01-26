import logging

from playwright.sync_api import Page, Locator

from lesson_29.page_objects.cart_page.cart_page import CartPage


class CartForm:

    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger(__name__)

    def get_cart_counter(self) -> int:
        cart_endicator: Locator = self.page.locator("span.shopping_cart_badge")
        number: str = cart_endicator.text_content()
        return int(number)

    def open_cart(self):
        self.page.locator("a.shopping_cart_link").click()
        return CartPage(self.page)
