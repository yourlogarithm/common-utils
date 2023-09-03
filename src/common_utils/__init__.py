import logging
from typing import Callable

from retry_async import retry
from retry_async.api import EXCEPTIONS


async def persistent_execution(func: Callable, *, exceptions: EXCEPTIONS = Exception, tries: int = -1, delay: float = 0, max_delay: float = None,
                               backoff: float = 1, logger_: logging.Logger, **kwargs):
    decorated_async_function = retry(is_async=True, exceptions=exceptions, tries=tries, delay=delay, max_delay=max_delay, backoff=backoff, logger=logger_)
    return await decorated_async_function(func, **kwargs)()
