# guessing game

import random

random_number = random.randint(1,10)

guess = None
while True:
    guess = int(input("Pick a number from 1 to 10: "))
    if random_number >  guess:
        print("You are too low...") 
    elif random_number <  guess:
        print("You are too high...")
    else:
        print("You won!!!")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            random_number = random.randint(1,10)
            guess = None
        else:
            print("Thnak you for playing. Bye...")
            break



print(random_number)
