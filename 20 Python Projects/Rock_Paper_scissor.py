import random 
 
def rps():
    exit = False

    while exit == False:
        option =['rock', 'paper', 'scissor']
        user_input = input('Choose Rock, Paper, Scissor or Exit: ')
        print("")
        computer_input = random.choice(option)
        exit = False 

        AI_score = 0
        Your_Score = 0 

        if user_input == 'exit':
            print("Game Ended")
            exit == True
            quit()
        
        if user_input == 'rock':
            if computer_input == 'rock':
                print("Computer input is rock")
                print('Your computer input is rock')
                print('draw')
            elif computer_input == 'paper':
                print('Computer input is paper.')
                print('Your input is Rock. ')
                print('Computer Won')
                AI_score += 1
            elif computer_input == 'scissor':
                print('Computer input is scissor.')
                print('Your input is Rock.')
                print('You Won')
                Your_Score += 1 
        if user_input == 'scissor':
            if computer_input == 'rock':
                print("Computer input is rock")
                print('Your input is scissor')
                print('Computer Win')
                AI_score += 1
            elif computer_input == 'paper':
                print('Computer input is paper.')
                print('Your input is Scissor. ')
                print('You Won')
                AI_score += 1
            elif computer_input == 'scissor':
                print('Computer input is scissor.')
                print('Your input is Scissor.')
                print('Draw') 
        if user_input == 'paper':
            if computer_input == 'rock':
                print("Computer input is rock")
                print('Your input is paper')
                print('You Won')
                Your_Score += 1
            elif computer_input == 'paper':
                print('Computer input is paper.')
                print('Your input is paper. ')
                print('Draw')
            elif computer_input == 'scissor':
                print('Computer input is scissor.')
                print('Your input is Paper.')
                print('Computer Won') 
                AI_score += 1
        print("")
        print('Computer Score: ', AI_score)
        print('Your Score: ', Your_Score)
        print("")
rps()