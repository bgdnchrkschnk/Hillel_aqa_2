import os
from playwright.sync_api import Page, Locator, expect

from lesson_29.page_objects.cart_form import CartForm
from lesson_29.page_objects.product_page.ProductPage import ProductPage


class HomePage:

    products_title_locator = "[data-test=title]"

    def __init__(self, page: Page):
        self.page = page
        self.url = os.getenv("SAUSEDEMO_BASE_URL") + "/inventory.html"
        self.cart_form: CartForm = CartForm(page)

    def click_on_product(self, place: int) -> ProductPage:
        element_locator = self.page.locator(".inventory_item_label a").all()[place-1]
        element_locator.click()
        return ProductPage(self.page)


    def click_add_to_cart_product(self, place: int) -> None:
        add_to_cart_button_locator = self.page.locator("div.inventory_list *.btn_inventory").all()[place-1]
        add_to_cart_button_locator.click()


    def is_logged_in(self) -> bool:
        try:
            expect(self.page).to_have_url(self.url)
            expect(self.page.locator(self.products_title_locator)).to_be_visible()
            return True
        except Exception:
            return False