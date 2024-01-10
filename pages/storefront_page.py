from playwright.async_api import Page
from pages.base_page import BasePage


class StorefrontPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def _checkout_button(self): return self.page.get_by_text('Checkout')
    def _create_user_button(self): return self.page.get_by_text('Create User')
    def _sign_in_user_button(self): return self.page.get_by_text('Sign In')
    def _product_cards(self): return self.page.locator(f"//div[@class='tile']")

    # Page methods

    async def go_to_checkout(self):
        return await self._checkout_button().click()

    async def go_to_create_user(self):
        return await self._create_user_button().click()

    def displayed_cards(self):
        return self._product_cards()

