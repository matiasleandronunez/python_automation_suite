from helpers import api_helper
from helpers.custom_exceptions import RequestUnexpected


async def setup_before_run():
    # Clear for new execution and set data, can't use hook because of parallel execution hack
    try:
        await api_helper.delete_all_customers()

    except RequestUnexpected:
        #Abort execution
        raise KeyboardInterrupt()

