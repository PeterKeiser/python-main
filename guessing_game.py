# guessing game

import random

random_number = random.randint(1,10)

guess = None
while guess != random_number:
    guess = int(input("Pick a number from 1 to 10: "))
    if random_number >  guess:
        print("You are too low...") 
    elif random_number <  guess:
        print("You are too high...")
    else:
        print("You won!!!")

print(random_number)
