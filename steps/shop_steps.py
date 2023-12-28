from behave import given, when, then
from behave import matchers
from behave.api.async_step import async_run_until_complete
from context.config import settings
from pages.base_page import BasePage
from pages.storefront_page import StorefrontPage

matchers.use_step_matcher("re")
from helpers import api_helper
from helpers.custom_exceptions import *


@async_run_until_complete
@given(u'I go to the storefront')
async def go_to_sf(context):
    base_page = BasePage(context.page)
    base_page.navigate(settings.url)


@async_run_until_complete
@when('I click on add (\d+) times for (.*)')
async def step_impl(context, times, tile_title):
    storefront_page = StorefrontPage(context.page)
    storefront_page.add_to_cart_by_item_name(tile_title, int(times))


@async_run_until_complete
@when(u'I proceed to checkout')
async def step_impl(context):
    context.storefront_page.checkout_cart()


@async_run_until_complete
@then(u'I verify (.*) was added to the cart (\d+) times')
async def step_impl(context, tile_title, times):
    assert context.checkout_page.get_cart_items()[tile_title] == int(times), f"expected {tile_title} to be added {times}, was {context.checkout_page.get_cart_items()[tile_title]}"


@async_run_until_complete
@then(u'I verify subtotal equals (\d+) by (\d+)')
async def step_impl(context, price, quantity):
    assert int(price) * int(quantity) == context.checkout_page.get_subtotal()


@async_run_until_complete
@then(u'I verify taxes amount \$1.50 by (\d+)')
async def step_impl(context, quantity):
    assert 1.5 * int(quantity) == context.checkout_page.get_taxes()


@async_run_until_complete
@then(u'I verify all items are displayed')
async def step_impl(context):
    assert len(api_helper.get_all_products()) == context.storefront_page.displayed_cards_count()