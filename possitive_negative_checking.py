# possitive negative checking

from random import randint
x = randint(-100, 100)
while x == 0:
    x = randint(-100, 100)
y = randint(-100, 100)
while y == 0:
    y = randint(-100, 100)
if x >= 1 and y >=1:
    print(f"both positive: {x}, {y}")
elif x <= -1 and y <= -1:
    print(f"both negative: {x}, {y}")
elif x >= 1 and y <= -1:
    print(f"x is positive and y is negative: {x}, {y}")
elif x <= -1 and y >= 1:
    print(f"x is negative and y is positive: {x}, {y}")