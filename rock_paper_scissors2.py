import random

options = ["paper", "rock", "scissors"]

game = True

player_score = 0
computer_score = 0

while game == True:

    
    computer_random = random.randint(0,2)

    print()
    player_choice = input("Choose between rock, paper and scissors: ")

    computer_choice = options[computer_random]

    print(f"Player: {player_choice} | Computer: {computer_choice}")
    print()


    if computer_choice == "paper" and player_choice == "rock":
        print("Computer win!")
        computer_score +=1
    elif computer_choice == "rock" and player_choice == "paper":
        print("You WIN!")
        player_score += 1
    elif computer_choice == "rock" and player_choice == "scissors":
        print("Computer win!")
        computer_score +=1
    elif computer_choice == "scissors" and player_choice == "rock":
        print("You WIN!")
        player_score += 1
    elif computer_choice == "scissors" and player_choice == "paper":
        print("Computer win!")
        computer_score +=1
    elif computer_choice == "paper" and player_choice == "scissors":
        print("You WIN!")
        player_score += 1
    elif computer_choice == player_choice:
        print("Tie...")
    elif player_choice == "exit":
        game = False
    elif player_choice != "paper" or "scissors" or "rock":
        print("Type only rock, paper and scissors!!!")


if player_score > computer_score:
    print(f"You win: Your score: {player_score} | Computer score: {computer_score}")
else:
    print(f"You lose: Computer score: {computer_score} | Your score: {player_score}")