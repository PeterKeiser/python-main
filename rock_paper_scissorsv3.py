# rock_paper_scissors

from random import randint
print("....Rock...")
print("....Paper...")
print("...Scissors...")

player = input("Player, make your move: ").lower()
rand_num = randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "scissors"
else:
    computer = "paper"
print(f"Computer plays: {computer}")

if player == "rock" and computer == "paper":
    print("computer wins")
elif player == "rock" and computer == "scissors":
    print("player wins")
elif player == "paper" and computer == "rock":
    print("player wins")
elif player == "paper" and computer == "scissors":
    print("computer wins")
elif player == "scissors" and computer == "paper":
    print("player wins")
elif player == "scissors" and computer == "rock":
    print("computer wins")
elif player == computer:
    print("It's a tie!")
else:
    print("Please enter a valid move.")