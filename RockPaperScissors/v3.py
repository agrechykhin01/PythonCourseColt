from random import randint

print("Rock...")
print("Paper...")
print("Scissors...")

rand_num = randint(0, 2)

if rand_num == 0:
    computer = "rock";
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"

player1 = input("Player 1, make your move: ").lower()

if player1 == computer:
    print("It's a tie!")
elif player1 == "rock":
    if computer == "scissors":
        print(f"Player1 wins! Computer chosen {computer}")
    else:
        print(f"computer wins and chosen {computer}!")
elif player1 == "scissors":
    if computer == "rock":
        print(f"computer wins and chosen {computer}!")
    else:
        print(f"Player1 wins! Computer chosen {computer}")
elif player1 == "paper":
    if computer == "rock":
        print(f"Player1 wins! Computer chosen {computer}")
    else:
        print(f"computer wins and chosen {computer}!")
else:
    print("Something went wrong!")
