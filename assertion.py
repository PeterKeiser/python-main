#  assertion

# def add_positive_numbers(x, y):
#     assert x > 0 and y > 0, "Both numbers must be positive!"
#     return x + y


# print(add_positive_numbers(1,2))
# print(add_positive_numbers(3, -1))


# def eat_junk(food):
#     assert food in ["Nutela", "ice creame", "pizza"], "Food must be an instance of junk food."
#     return f"Nom, nom, nom, I am eating {food}."


# food = input("Enter a food please: ")
# print(eat_junk(food))

# print(eat_junk("pizza"))
# print(eat_junk("banana"))

def do_something_bad(user):
    assert user.is_admin, "Only admins can do bad things!!!"
    return f"Mua ha ha {user} can do bad stuff."


user = input("Enter a role please: ")
print(do_something_bad(user))


