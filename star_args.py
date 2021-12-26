# star_args

# def sum_all_nums(num1, num2, num3):
#     return num1 + num2 + num3

# print(sum_all_nums(4, 6, 9))



# def sum_all_nums(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total 

# print(sum_all_nums(4,6,9, 4, 10))
# print(sum_all_nums(4,6,9))


def ensure_correct_info(*args):
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt!"
    return "Not sure who you are..."

print(ensure_correct_info("hello", False, 78))
print(ensure_correct_info(1, True, "Steele","Colt"))

