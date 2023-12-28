from behave import given, when, then
from behave import matchers
from behave.api.async_step import async_run_until_complete

from models.customer import Customer
from pages.storefront_page import StorefrontPage
from pages.user_page import CreateUserPage

matchers.use_step_matcher("re")
from helpers import api_helper
from helpers.custom_exceptions import *


@async_run_until_complete
@when(u'I go to the user creation screen')
async def step_impl(context):
    landing_page = StorefrontPage(context.page)
    landing_page.go_to_create_user


@async_run_until_complete
@when(u'I sign up a new user')
async def step_impl(context):
    user_create_page = CreateUserPage(context.page)
    context.user = Customer()
    user_create_page.input_user(name=context.user.username, password=context.user.password)
    user_create_page.click_sign_up_button


@async_run_until_complete
@then(u'I verify the new user account was created')
async def step_impl(context):
    assert context.user_create_page.is_success_message_displayed(), "Expected user creation success message to be displayed"
    assert api_helper.get_login_token(context.user).status_code == 200
