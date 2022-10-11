import random

dice_drawing = {
        1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),

    }

def roll_or_dice():
    
    roll = input("Roll the dice? (Yes/No): ")

    player_score = 0
    computer_score = 0

    while roll.lower() == "yes":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        computer_dice1 = random.randint(1, 6)
        computer_dice2 = random.randint(1, 6)

        print(f"You rolled: {dice1} and {dice2}")
        print()
        print("\n".join(dice_drawing[dice1]))
        print()
        print("\n".join(dice_drawing[dice2]))
        
        print()

        print(f"Computer rolled: {computer_dice1} and {computer_dice2}")
        print()
        print("\n".join(dice_drawing[computer_dice1]))
        print()
        print("\n".join(dice_drawing[computer_dice2]))

        if computer_dice1 and computer_dice2 > dice1 and dice2:
            print()
            print("Computer win!")
            computer_score = computer_score + 1
        else:
            print()
            print("You win!!!")
            player_score = player_score + 1

        roll = input("Roll again? (Yes/No:) ")
    
    print(f"Player score: {player_score} | Computer score: {computer_score}")
    if computer_score > player_score:
        print(f"Computer win. 🦾")
    else:
        print(f"Congrats you beat the computer!!! 💪")



roll_or_dice()