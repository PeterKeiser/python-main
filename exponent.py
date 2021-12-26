# exponent

# def exponent(num, power=2):
#     return num ** power

# print(exponent(2,5))
# print(exponent(3))
# print(exponent(7)) 

# def show_information(first_name="Colt", is_instructor=False):
#     if first_name == "Colt" and is_instructor:
#         return "Welcome back instructor Colt!"
#     elif first_name == "Colt":
#         return "I really tought you were an instructor..."
#     return f"Hello {first_name}!"

# print(show_information())
# print(show_information(is_instructor=True))
# print(show_information("Molly"))

def add(a, b):
    return a+b

# print(add(2,2))

def subtract(a,b):
    return a-b

# print(subtract(4,2))

def math(a, b, fn=add):
    return fn(a,b)

print(math(2,2,subtract))











