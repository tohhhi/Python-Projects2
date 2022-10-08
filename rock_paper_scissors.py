import random

i = 1

while i <= 10:
    i = i + 1
    
    player_choice = input("Choose rock, paper or scissors:")

    game_elements = ["rock", "paper", "scissors"]

    random_number = random.randint(0,2)

    computer_choice = (game_elements[random_number])

    print(f"Computer choice is {computer_choice} and player choice is {player_choice}.")

    if computer_choice == player_choice:
        print("Draw")
    elif computer_choice == "rock" and player_choice == "paper":
        print("You win.") 
    elif computer_choice == "paper" and player_choice == "rock":
        print("Computer win.")
    elif computer_choice == "scissors" and player_choice == "paper":
        print("Computer win.")
    elif computer_choice == "paper" and player_choice == "scissors":
        print("You win.")
    elif computer_choice == "rock" and player_choice == "scissors":
        print("Computer win.")
    elif computer_choice == "scissors" and player_choice == "rock":
        print("You win.")