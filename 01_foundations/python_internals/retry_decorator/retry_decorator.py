
import time
import functools
from typing import Callable, Tuple, Type 

def retry(
    retries: int = 3,
    delay: float = 1.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,)
):
    """
    Retry decorator.

    Args:
        retries: Number of retries before giving up
        delay: Delay between retries (seconds)
        exceptions: Exceptions to catch and retry on
    """

    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0

            while attempt <= retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt > retries:
                        print(f"[RETRY] Failed after {retries} retries")
                        raise
                    print(
                        f"[RETRY] Attempt {attempt}/{retries} failed: {e}. "
                        f"Retrying in {delay}s..."
                    )
                    time.sleep(delay)

        return wrapper

    return decorator