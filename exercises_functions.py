# exercises_functions

# def product(a, b):
#     return a * b

# print(product(2,2))
# print(product(2,-2))

# def return_day(number_of_day):
#     if number_of_day == 1:
#         return "Sunday"
#     elif number_of_day == 2:
#         return "Monday"
#     elif number_of_day == 3:
#         return "Tuesday"
#     elif number_of_day == 4:
#         return "Wednesday" 
#     elif number_of_day == 5:
#         return "Thursday"
#     elif number_of_day == 6:
#         return "Friday"
#     elif number_of_day == 7:
#         return "Saturday"
#     else:
#         return "None"

# print(return_day(1))
# print(return_day(7))
# print(return_day(-1))
# print(return_day(0))
# print(return_day(8))
# print(return_day(7))


# def return_day(number_of_day):
#     number_of_day = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
#     return number_of_day

# print(return_day(2))

# def return_day(num):
#     days = ["Sunday", "Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#     if num > 0 and num <= len(days):
#         return days[num-1]
#     return None

# print(return_day(1))
# print(return_day(7))
# print(return_day(-1))
# print(return_day(0))
# print(return_day(8))
# print(return_day(7))


def return_day(num):
    try:
        return ["Sunday", "Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] [num-1]
    except IndexError as e:
        return None

print(return_day(1))
print(return_day(7))
print(return_day(-1))
print(return_day(0))
print(return_day(8))
print(return_day(7))






