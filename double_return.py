# double_return

from functools import wraps

def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        val = fn(*args, **kwargs)
        return [val, val]
    return wrapper


@double_return
def add(x, y):
    return x + y

@double_return
def greet(name):
    return f"Hi, I am {name}."


print(add(2, 3))
print(greet("Colt"))








