# divide

def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError as err: 
        print("don't divide by zero")
        print(err)
    except TypeError as err:
        print("A and B must be ints or floats")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")


    
print(divide(1,2))
print(divide(1,0))
print(divide(1,"c"))
