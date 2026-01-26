import os
from playwright.sync_api import Page, Locator, expect




class ProductPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = os.getenv("SAUSEDEMO_BASE_URL") + "/inventory-item.html?id="
        from lesson_29.page_objects.cart_form import CartForm
        self.cart_form: CartForm = CartForm(page)

    @property
    def back_to_products(self) -> Locator:
        return self.page.locator("#back-to-products")

    @property
    def add_to_cart_button(self) -> Locator:
        return self.page.locator("#add-to-cart")

    def is_page_opened(self) -> bool:
        try:
            expect(self.page).to_have_url(self.url)
            expect(self.back_to_products).to_be_visible()
            return True
        except Exception:
            return False

    def add_to_cart(self) -> None:
        self.add_to_cart_button.click()

