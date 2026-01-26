import os
from playwright.sync_api import Page, Locator, expect


from lesson_29.page_objects.product_page.ProductPage import ProductPage


class CartPage:


    def __init__(self, page: Page):
        self.page = page
        self.url = os.getenv("SAUSEDEMO_BASE_URL") + "/cart.html"
        from lesson_29.page_objects.cart_form import CartForm
        self.cart_form: CartForm = CartForm(page)

    def get_items_in_cart(self) -> int:
        items_number = self.page.locator("div.inventory_item_name").count()
        return items_number