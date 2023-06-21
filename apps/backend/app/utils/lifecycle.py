import asyncio
from loguru import logger


async def do_stuff_periodically(interval, periodic_function):
    """
    This function executes a given function periodically at a specified interval using asyncio.

    :param interval: The time interval (in seconds) at which the periodic function should be executed
    :param periodic_function: `periodic_function` is a function that will be executed periodically at a
    fixed interval specified by the `interval` parameter. This function can be any coroutine function
    that you want to execute periodically
    """
    try:
        while True:
            await asyncio.gather(
                asyncio.sleep(interval),
                periodic_function(),
            )
    except Exception:
        logger.info("periodic_task stop")
