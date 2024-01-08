from playwright.async_api import Page
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def _quantity_span(self, product_title): return self.page.locator(f"//div[text()='{product_title}']/following-sibling::div/span[contains(text(),'Quantity')]")
    def _product_individual_price(self, product_title): return self.page.locator("//div[text()='#{product_title}']/ancestor::div[@class='productItem']//div[@class='columnRight']")
    def _total_amount(self): return self.page.locator("//div[@class='totalFinal']//span[text()='Total']/following-sibling::span")
    def _subtotal_amount(self): return self.page.locator("//div[@class='totalDetails']//span[text()='subtotal']/following-sibling::span")
    def _taxes_amount(self): return self.page.locator("//div[@class='totalDetails']//span[text()='taxes']/following-sibling::span")
    def _shipping_amount(self): return self.page.locator("//div[@class='totalDetails']//span[text()='shipping']/following-sibling::span")

    # Page methods
    async def product_quantity_in_cart(self, product_title):
        return await (self._quantity_span(product_title)).inner_text()

    async def product_price_in_cart(self, product_title):
        return await self._price_string_to_f((self._product_individual_price(product_title)).inner_text())

    async def cart_subtotal(self):
        return await self._price_string_to_f((self._subtotal_amount()).inner_text())

    async def cart_shipping(self):
        return await self._price_string_to_f((self._shipping_amount()).inner_text())

    async def cart_taxes(self):
        return await self._price_string_to_f((self._taxes_amount()).inner_text())

    async def cart_total(self):
        return await self._price_string_to_f((self._total_amount()).inner_text())

