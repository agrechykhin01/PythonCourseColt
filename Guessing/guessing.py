from random import randint

random_number = randint(1,10)

while True:
    guess = int(input("Pick a number from 1 to 10: "))
    if guess > random_number:
        print("TOO HIGH!")
    elif guess < random_number:
        print("TOO LOW!")
    else:
        print("YOU GOT IT!")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == "y":
            random_number = randint(1, 10)
        else:
            print("Thank you for playing!")
            break
        
