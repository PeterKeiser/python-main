# food

from random import choice
food = choice(["apple", "grape", "bacon", "steak", "worm", "dirt"])

if food == "apple" or food == "grape":
    print(f"{food}: fruit")
elif food == "bacon" or food == "steak":
    print(f"{food}: meat")
else:
    print(f"{food}: yuck")