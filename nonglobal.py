# nonglobal

# def outer():
#     count = 0
#     def inner():
#         nonlocal count 
#         count +=1
#         return count
#     # return inner()
#     return outer()

# print(outer())
# print(outer())
# print(outer())
# print(outer())

def say_hello():
    """A simple function that returns the string hello"""
    return "Hello!"

print(say_hello())

import random

print(say_hello.__doc__)
print(random.randint.__doc__)