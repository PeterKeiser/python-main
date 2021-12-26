# dictionary comprehention

# numbers = dict(first=1, second=2, third=3)
# print(numbers)

# squared_numbers = {key:value ** 2 for key,value in numbers.items()}
# print(squared_numbers)

# nums = [1, 2, 3, 4, 5]
# print(nums)

# squared_nums = {num: num ** 2 for num in [1, 2, 3, 4, 5]}
# print(squared_nums)

str1 = "ABC"
print(str1)
str2 = "123"
print(str2)

combo = {str1[i]: str2[i] for i in range(0, len(str1))}
print(combo)



