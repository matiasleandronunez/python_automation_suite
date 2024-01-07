from behave import fixture, use_fixture
from behave.api.async_step import async_run_until_complete
from playwright.async_api import async_playwright
from helpers import api_helper
from helpers.custom_exceptions import RequestUnexpected, RequestReturnedNonOK
from models.customer import Customer


@fixture
async def browser_chrome(context):
    p = await async_playwright().start()
    browser = await p.chromium.launch(headless=False, slow_mo=1000, channel="chrome")
    context.page = await browser.new_page()
    return context.page


@async_run_until_complete
async def before_scenario(context, scenario):
    if 'api_existing_customer' in scenario.tags:
        context.existing_customer = Customer()
        await api_helper.post_customer(context.existing_customer)
    elif 'api_add_new_customer' in scenario.tags:
        context.to_update = await api_helper.post_customer(Customer())
    elif 'api_delete_customer' in scenario.tags:
        context.to_delete = await api_helper.post_customer(Customer())

    await use_fixture(browser_chrome, context)
