import asyncio

from behave import given, when, then
from behave import matchers
from behave.api.async_step import async_run_until_complete
matchers.use_step_matcher("re")
from helpers import api_helper
from helpers.custom_exceptions import *


@given(u'I post an existing customer to the customer create endpoint')
@async_run_until_complete
async def step_impl(context):
    try:
        await api_helper.post_customer(context.existing_customer)
    except RequestUnexpected as e:
        context.exc = e


@then(u'I verify I get a conflict response from the API')
@async_run_until_complete
async def step_impl(context):
    assert context.exc is not None
    assert isinstance(context.exc, RequestReturnedConflict)


@given(u'I delete a customer to the customer delete endpoint')
@async_run_until_complete
async def step_impl(context):
    context.response_httpcode = await api_helper.delete_customer(context.to_delete)


@then(u'I verify I get a no content response from the API')
@async_run_until_complete
async def step_impl(context):
    assert context.response_httpcode == 204


@given(u'I post a new customer to the customer create endpoint')
@async_run_until_complete
async def step_impl(context):
    context.response_id = await api_helper.post_customer()


@then(u'I verify I get the customer ID from the API response')
@async_run_until_complete
async def step_impl(context):
    assert int(context.response_id) > 0
