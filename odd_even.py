# odd or even

from random import randint
num = randint(1,1000)
if num % 2 == 0:
    print(f" {num} even")
else:
    print(f"{num} odd")