# greatest_magnitude



def max_magnitude(nums):
    return  max(abs(num) for num in nums)

print(max_magnitude([1, 2, 3]))
print(max_magnitude([-200, 201, -903]))