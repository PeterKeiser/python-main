# is_all_strings

# def is_all_strings(lst):
#     return all(type(l) == str for l in lst)

# print(is_all_strings(["a", "b", "c"]))
# print(is_all_strings([2, "a", "b", "c"]))
# print(is_all_strings(["hello", "goodbye"]))


def is_all_strings2(list2):
    return all([type(l) == str for l in list2])


print(is_all_strings2(["a", "b", "c"]))
print(is_all_strings2([2, "a", "b", "c"]))
print(is_all_strings2(["hello", "goodbye"]))