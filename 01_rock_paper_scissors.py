from random import randint 

play_again: bool = True

while play_again:
    play_again: bool = False
    print("Rock...")
    print("Paper...")
    print("Scissors...")
    print("Shoot!")

    player_1: str = input("Player, make your move: ").lower()

    random_choice: int = randint(0,2)

    if random_choice == 0:
        computer: str = "rock"
    elif random_choice == 1:
        computer: str = "paper"
    else:
        computer: str = "scissors"

    print(f"Computer plays {computer}")

    if player_1 == computer:
        print("It's a draw!")
    elif player_1 == "rock":
        if computer == "scissors":
            print(f"{player_1.capitalize()} beats {computer}, Player wins!")
        elif computer == "paper":
            print(f"{computer.capitalize()} beats {player_1}, Computer wins!")
    elif player_1 == "paper":
        if computer == "rock":
            print(f"{player_1.capitalize()} beats {computer}, Player wins!")
        elif computer == "scissors":
            print(f"{computer.capitalize()} beats {player_1}, Computer wins!")
    elif player_1 == "scissors":
        if computer == "paper":
            print(f"{player_1.capitalize()} beats {computer}, Player wins!")
        elif computer == "rock":
            print(f"{computer.capitalize()} beats {player_1}, Computer wins!")
    else:
        print("You are playing the game wrong. Make a valid move silly!")

    new_game: bool = input("Would you like to play again? If so enter 'yes' ").lower()

    if new_game == "yes":
        play_again = True