from playwright.async_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    async def navigate(self, uri):
        await self.page.goto(uri)

    # Private cross-Pages utility methods
    def _price_string_to_f(self, price_s):
        return float(price_s.replace("$","").replace(",",""))