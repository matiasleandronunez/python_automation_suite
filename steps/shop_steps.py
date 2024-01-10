from behave import given, when, then
from behave import matchers
from behave.api.async_step import async_run_until_complete
from playwright.async_api import expect

from context.config import settings
from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage
from pages.storefront_page import StorefrontPage
from pages.product_card_section import ProductCardSection

matchers.use_step_matcher("re")

from helpers import api_helper
from helpers.custom_exceptions import *


@given(u'I go to the storefront')
@async_run_until_complete
async def go_to_sf(context):
    base_page = BasePage(context.page)
    await base_page.navigate(settings.url)
    storefront_page = StorefrontPage(context.page)
    context.storefront_page = storefront_page


@when("I click on add (\d+) times for (.*)")
@async_run_until_complete
async def step_impl(context, times, tile_title):
    context.product_card = ProductCardSection(context.page, tile_title)
    await context.product_card.click_add(int(times))


@when(u'I proceed to checkout')
@async_run_until_complete
async def step_impl(context):
    await context.storefront_page.go_to_checkout()
    context.checkout_page = CheckoutPage(context.page)


@then(u'I verify (.*) was added to the cart (\d+) times')
@async_run_until_complete
async def step_impl(context, tile_title, times):
    assert (await context.checkout_page.product_quantity_in_cart(tile_title)) == int(times), f"expected {tile_title} to be added {times}, was {await context.checkout_page.product_quantity_in_cart(tile_title)}"


@then(u'I verify subtotal equals (\d+) by (\d+)')
@async_run_until_complete
async def step_impl(context, price, quantity):
    assert int(price) * int(quantity) == await context.checkout_page.cart_subtotal()


@then(u'I verify taxes amount \$1.50 by (\d+)')
@async_run_until_complete
async def step_impl(context, quantity):
    assert 1.5 * int(quantity) == await context.checkout_page.cart_taxes()


@then(u'I verify all items are displayed')
@async_run_until_complete
async def step_impl(context):
    await expect(context.storefront_page.displayed_cards()).to_have_count(len(await api_helper.get_all_products()))



