# show_args

from math import floor
from functools import wraps

def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Here are the args: ", args)
        print("Here are the kwargs: ", kwargs)
        return fn(*args, **kwargs)
    return wrapper


@show_args
def do_nothing(*args, **kwargs):
    pass

# show_args(floor)
print(do_nothing(1, 2, 3, 4, a="hi", b="bye"))

# 1, 2, 3, 4, a="hi", b="bye"


