# unlucky_numbers

# for n in range(1,21):
#     if n == 4 or n == 13:
#         print(f"{n} IS UNLUCKY!")
#     elif n % 2 != 0:
#         print(f"{n} is odd")
#     elif n % 2 == 0:
#         print(f"{n} is even")
    
for n in range(1,21):
    if n == 4 or n == 13:
        state = "IS UNLUCKY"
    elif n % 2 != 0:
        state = "is odd"
    elif n % 2 == 0:
        state = "is even"
    print(f"{n} {state}")
    