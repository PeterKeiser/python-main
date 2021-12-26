# debugging

def divide(num1,num2):
    try:
        result = num1/num2
    except TypeError:
        print("Please provide integars of floats for num1 and num2")
    except ZeroDivisionError:
        print("Please don't divide by zero")
    else:
        print(f"{num1} divided by {num2} is {result}")


print(divide(1,2))
print(divide(1,0))
print(divide(1,"w"))
    