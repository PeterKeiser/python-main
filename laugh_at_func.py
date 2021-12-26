# laugh_at_func

from random import choice

def make_laugh_st_func(person):
    def get_laugh():
        laugh = choice (("HAHAHAHA", "lol", "thehehe"))
        return f"{laugh} {person}"

    return get_laugh
laugh_at = make_laugh_st_func("Linda")


print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())

