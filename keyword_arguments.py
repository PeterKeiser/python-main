# keyword_arguments

# def full_name (first, last):
#     return f"Your name it {first} {last}"

# print(full_name("Peter", "Muller."))
# print(full_name(last = "Muller.", first = "Peter"))



def full_name2 (first="Colt", last="Steele"):
    return f"Your name is {first} {last}."

print(full_name2())
print(full_name2(first = "Peter", last = "Muller"))
print(full_name2(last = "Muller", first = "Peter"))



