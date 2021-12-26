# return

# def print_square_of_7():
#     print(7 ** 2)

# print_square_of_7()

def square_of_7():
    7 ** 2
result = square_of_7()

print(result)

#####    BUT   ##########

def square_of_7():
    return 7 ** 2
result = square_of_7()

print(result)

def say_hi():
    print("I am BEFORE the return...")
    return "Hi!!!"
    print("I am after the return...")

greeting = say_hi()
print(greeting)