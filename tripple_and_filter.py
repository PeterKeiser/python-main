# tripple_and_filter

# def tripple_and_filter(nums):
#         for num in nums if num % 4 != 0:

def tripple_and_filter(nums):
    return list(filter(lambda num: num % 4 == 0, map(lambda num: num * 3, nums)))


print(tripple_and_filter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]))


