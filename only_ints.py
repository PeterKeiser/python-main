# only_ints

from functools import wraps

def only_ints(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # if ([arg for arg in args if type(arg) != int]):
        if ([arg for arg in args if not isinstance(arg, int)]):
            return "Please only invoke with integers."
        return fn(*args, **kwargs)
    return wrapper


@only_ints
def add(x, y):
    return x + y

print(add(2, 7))
print(add(3.678, 13.556))
      






