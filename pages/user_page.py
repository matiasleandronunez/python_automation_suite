from playwright.async_api import Page
from pages.base_page import BasePage

class CreateUserPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def _username_input(self): return await self.page.locator(css="input[name=username]")
    async def _password_input(self): return await self.page.locator(css="input[name=password]")
    async def _sign_up_button(self): return await self.page.locator(css="div.createFormButton button")

    # Page methods
    async def input_user(self, name='someone', password='qwerty12'):
        await self._username_input.fill(name)
        await self._password_input.fill(password)


    async def click_sign_up_button(self):
        await self._signup_button.click()
