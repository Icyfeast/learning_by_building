import random
from retry_decorator import retry


@retry(retries=3, delay=2, exceptions=(ValueError,))
def flaky_service():
    print("Calling flaky service...")
    t = random.random()
    if t < 0.4:
        raise ValueError("Value failure occurred")
    elif t < 0.6:
        raise TypeError("Type failure occurred")
    elif t < 0.8:
        raise Exception("Exception failure occurred")
    return "Success!"


if __name__ == "__main__":
    result = flaky_service()
    print("Result:", result)
