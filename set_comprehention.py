# set comprehention

nums = {x **  2 for x in range(10)}
print(nums)

nums2 = {x: x ** 2 for x in range(10)}
print(nums2)

cahracters = {char.upper() for char in "hello"}
print(cahracters)

def all_vowels_in_string(string):
    return len({char for char in string if char in "aeiou"}) == 5