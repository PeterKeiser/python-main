# delay

from functools import wraps
from time import sleep

def delay(timer):
    def inner(fn):
        @wraps(fn)
        def wrapper (*args, **kwargs):
            print(f"Waiting {timer}s before running {fn}")
            sleep(timer)
            return fn(*args, **kwargs)
        return wrapper
    return inner

@delay(5)
def say_hi():
    return "hi"


print(say_hi())

