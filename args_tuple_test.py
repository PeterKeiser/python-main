# args_tuple_test

def contains_purple(*args):
    if "purple" in args:
        return True, args
    return False, args

print(contains_purple(1, 2, 3, "purple"))


# def contains_purple(*args):
#     if "purple" in args: 
#         return True, args
#     return False, args

# print(contains_purple(1, 2, 3, "purple"))
