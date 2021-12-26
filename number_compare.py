# number_compare

def number_compare(num1, num2):
    if num1 > num2:
        return "First number is greater"
    elif num1 < num2:
        return "Second number is greater"
    else:
        return "Numbers are equal"


print(number_compare(1,2))
print(number_compare(2,2))
print(number_compare(2,1))
