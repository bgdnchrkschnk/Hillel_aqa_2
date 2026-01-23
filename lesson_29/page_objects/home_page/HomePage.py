import os
from playwright.sync_api import Page, Locator, expect


class HomePage:

    products_title_locator = "[data-test=title]"

    def __init__(self, page: Page):
        self.page = page
        self.url = os.getenv("SAUSEDEMO_BASE_URL") + "/inventory.html"

    def click_on_product(self, place: int) -> None:
        element_locator = self.page.locator(".inventory_item_label a").all()[place-1]
        element_locator.click()
        # return self.page.locator(".inventory_item_label a").nth(place-1)

    def is_logged_in(self) -> bool:
        try:
            expect(self.page).to_have_url(self.url)
            expect(self.page.locator(self.products_title_locator)).to_be_visible()
            return True
        except Exception:
            return False