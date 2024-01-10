from playwright.async_api import Page, expect
from pages.base_page import BasePage

class CreateUserPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def _username_input(self): return self.page.locator("input[name=username]")
    def _password_input(self): return self.page.locator("input[name=password]")
    def _sign_up_button(self): return self.page.locator("div.createFormButton button")
    def _success_message(self): return self.page.locator("div.successMessage")

    # Page methods
    async def input_user(self, name='someone', password='qwerty12'):
        await self._username_input().fill(name)
        await self._password_input().fill(password)

    async def click_sign_up_button(self):
        await self._sign_up_button().click()

    def success_message(self):
        return self._success_message()

