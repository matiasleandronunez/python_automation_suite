from playwright.async_api import Page
from pages.base_page import BasePage

class ProductCardSection(BasePage):
    def __init__(self, page: Page, card_title, card_id=None):
        super().__init__(page)
        self.id = card_id
        self.card_title = card_title


    async def _product_card_base(self): return await self.page.locator(f"//div[@class='tile'][div[contains(text(),\"{self.card_title}\")]][div[@class='tileImage']]")
    def _add_button(self): return self._product_card_base().locator("//div[@class='tileAdd']")
    def _price(self): return self._product_card_base().locator("//div[@class='tilePrice']")

    # Page methods
    async def click_add(self, quantity):
        for i in range(1, quantity + 1):
            await self._add_button.click()

    async def is_visible(self):
        return await self._product_card_base.is_visible()
