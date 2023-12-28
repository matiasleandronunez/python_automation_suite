from playwright.async_api import Page
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def _quantity_span(self, product_title): return await self.page.locator(f"//div[text()='{product_title}']/following-sibling::div/span[contains(text(),'Quantity')]")
    async def _product_individual_price(self, product_title): return await self.page.locator("//div[text()='#{product_title}']/ancestor::div[@class='productItem']//div[@class='columnRight']")
    async def _total_amount(self): return await self.page.locator("//div[@class='totalFinal']//span[text()='Total']/following-sibling::span")
    async def _subtotal_amount(self): return await self.page.locator("//div[@class='totalDetails']//span[text()='subtotal']/following-sibling::span")
    async def _taxes_amount(self): return await self.page.locator("//div[@class='totalDetails']//span[text()='taxes']/following-sibling::span")
    async def _shipping_amount(self): return await self.page.locator("//div[@class='totalDetails']//span[text()='shipping']/following-sibling::span")

    # Page methods
    async def product_quantity_in_cart(self, product_title):
        return await self._quantity_span(product_title).inner_text()

    async def product_price_in_cart(self, product_title):
        return self._price_string_to_f(await self._product_individual_price(product_title).inner_text())

    async def cart_subtotal(self):
        return self._price_string_to_f(await self._subtotal_amount.inner_text())

    async def cart_shipping(self):
        return self._price_string_to_f(await self._shipping_amount.inner_text())

    async def cart_taxes(self):
        return self._price_string_to_f(await self._taxes_amount.inner_text())

    async def cart_total(self):
        return self._price_string_to_f(await self._total_amount.inner_text())
