# add_and_multiply_numbers

def add_and_multiply_numbers(a, b, c, **kwargs):
    return a + b * c
    print("other stuff....")
    print(kwargs)

data = dict(a=1, b=2, c=3, d=55, name="Tony")

# print(add_and_multiply_numbers(data))
print(add_and_multiply_numbers(**data, cat="blue"))

