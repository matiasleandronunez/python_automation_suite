from helpers import before_run_hooks
import asyncio

if __name__ == '__main__':
    # SETUP HOOKS
    loop = asyncio.get_event_loop()
    loop.run_until_complete(before_run_hooks.setup_before_run())

    from behave import __main__ as behave_executable
    behave_executable.main(None)
