from random import randint 

player_wins: int = 0
computer_wins: int = 0

while player_wins < 2 and computer_wins < 2:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
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
            player_wins += 1
        elif computer == "paper":
            print(f"{computer.capitalize()} beats {player_1}, Computer wins!")
            computer_wins += 1
    elif player_1 == "paper":
        if computer == "rock":
            print(f"{player_1.capitalize()} beats {computer}, Player wins!")
            player_wins += 1
        elif computer == "scissors":
            print(f"{computer.capitalize()} beats {player_1}, Computer wins!")
            computer_wins += 1
    elif player_1 == "scissors":
        if computer == "paper":
            print(f"{player_1.capitalize()} beats {computer}, Player wins!")
            player_wins += 1
        elif computer == "rock":
            print(f"{computer.capitalize()} beats {player_1}, Computer wins!")
            computer_wins += 1
    else:
        print("You are playing the game wrong. Make a valid move silly!")
print(f"FINAL SCORES... Player: {player_wins} Computer: {computer_wins}")