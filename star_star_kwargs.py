# star_star_kwargs


# def fev_colours(**kwargs):
#     for person, colour in kwargs.items():
#         print(f"{person}'s favourite colour is {colour}.")
    
# print(fev_colours(colt="purple", ruby="red", ethel="teal"))
# print(fev_colours(colt="purple", ruby="red", ethel="teal", ted="blue"))
# print(fev_colours(colt="royal deep amazing purple"))


def special_greeting(**kwargs):
    if "David" in kwargs and kwargs ["David"]== "special":
        return "You get a special greeting David!"
    elif "David" in kwargs:
        return f"{kwargs['David']} David!"
    return "Not sure who this is..."

print(special_greeting(David="Hello"))
print(special_greeting(Bob="hello"))
print(special_greeting(David="special"))