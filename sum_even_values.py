# sum_even_values

# def sum_even_values(values):
#     result=0
#     (val for val in values if val % 2 == 0):
#     return result += val


def sum_even_valued(values):
    return sum(val for val in values if val % 2 ==0)

print(sum_even_valued([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))


def sum_even_valued(*args):
    return sum(arg for arg in args if arg % 2 ==0)

print(sum_even_valued(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))




