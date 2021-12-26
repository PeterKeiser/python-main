# activities 

from random import choice

def eat(food, is_healthy):
    if not isinstance(is_healthy, bool):
        raise ValueError("is_healthy mus be aboolean")
    ending = "because YOLO!"
    if is_healthy:
        ending = "because my body is atemple."
    return f"I am eating {food}, {ending}"

def nap(num_hours):
    if num_hours >= 2:
        return f"Ugh I overslept. I did not mean to nap for {num_hours} hours!"
    return f"I am feeling refreshed after my {num_hours} hour nap."

def is_funny(person):
    if person is "tim": return False
    return True

def laugh():
    return choice(("lol", "haha", "thehe"))













