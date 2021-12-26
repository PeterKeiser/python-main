# ensure_authorised

from functools import wraps

def ensure_authorised(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return fn(*args, **kwargs)
        return "Unauthorised"
    return wrapper


@ensure_authorised
def show_secrets(*args, **kwargs):
    return "Shh..! Don't tell anybody"


print(show_secrets(role = "admin"))
print(show_secrets(role = "nobody"))
print(show_secrets(a = "b"))






