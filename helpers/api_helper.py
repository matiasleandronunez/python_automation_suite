import os

from playwright.async_api import async_playwright

from context.config import settings
from types import SimpleNamespace
import json
from helpers.custom_exceptions import *
from models.customer import Customer


async def _get_request_context():
    p = await async_playwright().start()
    return await p.request.new_context(base_url=settings.api_uri)


async def get_customer_by_username(username):
    context = await _get_request_context()
    response = await context.get(f"/api/customer/username={username}")

    if response.status != 200:
        raise RequestReturnedNonOK(response.status)
    else:
        return json.loads(response.json(), object_hook=lambda d: SimpleNamespace(**d))


async def get_login_token(customer):
    req_body = json.dumps({
                "username": f"{customer.username}",
                "password": f"{customer.password}"
    }, indent=4)

    req_headers = {'Content-type': 'application/json'}

    context = await _get_request_context()
    response = await context.post(f"/login/", data=req_body, headers=req_headers)

    if response.status != 200:
        raise RequestReturnedNonOK(response.status)
    else:
        return response.status


async def post_customer(customer=None):
    customer = customer if customer is not None else Customer()

    req_body = json.dumps({"customerId": 0,
        "name": f"{customer.name}",
        "address": f"{customer.addr}",
        "email": f"{customer.email}",
        "phone": f"{customer.phone}",
        "username": f"{customer.username}",
        "password": f"{customer.password}",
        "enabled": "true",
        "role": "USER"}, indent=4)

    req_headers = {'Content-type': 'application/json'}

    context = await _get_request_context()
    response = await context.post(f"/api/customer/", data=req_body, headers=req_headers)

    if response.status != 201:
        if response.status == 409:
            raise RequestReturnedConflict(status_code=response.status)
        else:
            raise RequestReturnedNonOK(status_code=response.status)
    else:
        res = await response.text()
        return json.loads(res)['customerId']


async def delete_all_customers():
    context = await _get_request_context()
    response = await context.delete(f"/api/customer/")

    if response.status != 204:
        raise RequestReturnedNonExpected(response.status)
    else:
        return response.status


async def delete_customer(cust_id):
    context = await _get_request_context()
    response = await context.delete(f"/api/customer/{cust_id}")

    if response.status != 204:
        raise RequestReturnedNonExpected(response.status)
    else:
        return response.status


async def get_all_products():
    context = await _get_request_context()
    response = await context.get(f"/api/product/")

    if response.status == 200:
        return response.json()
    elif response.status == 204:
        return []
    else:
        raise RequestReturnedNonOK(response.status)
