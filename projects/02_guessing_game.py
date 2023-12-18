from random import randint

random_number: int = randint(1, 10)

while True:
    guess: str = input("Pick a number from 1 to 10: ")
    guess: int = int(guess)
    if guess < random_number:
        print("TOO LOW!")
    elif guess > random_number:
        print("TOO HIGH!")
        play_again: str = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            random_number: int = randint(1, 10)
            guess: int = None
        else:
            print("Thank you for playing!")
            break
