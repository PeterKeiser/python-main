# rock_paper_scissors

from random import randint

player_wins = 0
computer_wins = 0
winning_score = 3
while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player Score: {player_wins}, Computer Score: {computer_wins}")
    print("....Rock...")
    print("....Paper...")
    print("...Scissors...")

    player = input("Player, make your move: ").lower()
    if player == "quit" or player == "q":
        break
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
        computer_wins += 1
    elif player == "rock" and computer == "scissors":
        print("player wins")
        player_wins += 1
    elif player == "paper" and computer == "rock":
        print("player wins")
        player_wins += 1
    elif player == "paper" and computer == "scissors":
        print("computer wins")
        computer_wins += 1
    elif player == "scissors" and computer == "paper":
        print("player wins")
        player_wins += 1
    elif player == "scissors" and computer == "rock":
        print("computer wins")
        computer_wins += 1
    elif player == computer:
        print("It's a tie!")
    else:
        print("Please enter a valid move.")
if player_wins > computer_wins:
    print("CONGRATS, YOU WON!")
elif player_wins == computer_wins:
    print("IT'S A TIE")
else:
    print("OH NO :( the computer won...")
print(f"FINAL SCORES: Player Score: {player_wins}, Computer Score: {computer_wins}")