# get_unlimited_multiples


def get_unlimited_multiples(num=1):
    next_number = num
    while True:
        yield next_number
        next_number += num


result = get_unlimited_multiples(5)
#  print(result)
print(next(result))
print(next(result))
print(next(result))
print(next(result))


