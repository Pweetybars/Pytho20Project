#import random 
# define a roll dice function 
# create a dictonary with the dice drawing 

import random

def roll_dice():
    
    dice_drawing = {
       1: (  
        "┌─────────┐",  
        "│   1     │",  
        "│    ●    │",  
        "│         │ ",  
        "└─────────┘",  
    ),  
    2: (  
        "┌─────────┐",  
        "│    ●    │",  
        "│    2    │",  
        "│    ●    │",  
        "└─────────┘",  
    ),  
    3: (  
        "┌─────────┐",  
        "│ ●     3 │",  
        "│    ●    │",  
        "│       ● │",  
        "└─────────┘",  
    ),  
    4: (  
        "┌─────────┐",  
        "│ ●     ● │",  
        "│    4    │",  
        "│ ●     ● │",  
        "└─────────┘",  
    ),  
    5: (  
        "┌─────────┐",  
        "│ ●  5  ● │",  
        "│    ●    │",  
        "│ ●     ● │",  
        "└─────────┘",  
    ),  
    6: (  
        "┌─────────┐",  
        "│ ●     ● │",  
        "│ ●   6 ● │",  
        "│ ●     ● │",  
        "└─────────┘",  
    ),  
    }
    roll = input("Roll dice? (Yes/No)")

    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        print("Dice roll: {} and {}".format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        roll = input("Roll again? (Yes,No): ")

roll_dice()