# filter2

nums = [1, 2, -3, 4, -55, 6]

def remove_negatives(num):
    return list(filter(lambda num: num >= 0, nums))

print(remove_negatives(nums))


