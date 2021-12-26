# state abbreviations

# list1 = ["CA", "NJ", "RI"]
# print(list1)
# list2 = ["California", "New Jersey", "Rhode Island"]
# print(list2)

# answers = {list1[i]: list2[i] for i in range(0, 3)}
# print(answers)

list1 = ["CA", "NJ", "RI"]
print(list1)
list2 = ["California", "New Jersey", "Rhode Island"]
print(list2)

answers = dict(zip(list1, list2))
print(answers)
