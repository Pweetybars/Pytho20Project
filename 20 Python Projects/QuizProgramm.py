quiz = {
    'question1' : {
        'question' : 'What is the capital of Cambodia?',
        'answer' : 'Phnom Penh'
    }, 
    'question2' : {
       'question' : 'What is the capital of Germany?',
       'answer' : 'Berlin' 
    }, 
    'question3' : {
       'question' : 'What is the capital of Japan?',
       'answer' : 'Tokyo' 
    }, 
    'question4' : {
       'question' : 'What is the capital of Spain?',
       'answer' : 'Madrid' 
    }, 
    'question5' : {
       'question' : 'What is the capital of Portugal?',
       'answer' : 'Lisbon' 
    },
    'question6' : {
       'question' : 'What is the capital of Switzerland?',
       'answer' : 'Zurich' 
    }, 
    'question7' : {
       'question' : 'What is the capital of Thailand?',
       'answer' : 'Bangkok' 
    }, 
}
#create a dictionary that store queestion and answer 

score = 0
#create a variable to track the score 

for key, value in quiz.items():
#loop through that dictionary using key value pairs 
    print(value['question'])
    answer  = input("Answer: ")
    # display each question to the user and allow them to answer 
    if answer.lower() == value['answer'].lower():
        print("Correct")
        score += 1 
        print('Your score is: '+str(score))
        print("")
    else :
        print("Wrong")
        print('The answer is: '+value['answer'])
        print('Your score is: '+str(score))
        print("")
    # tell them if they are right or wrong

print("You got "+str(score)+" out of 7 question correctly.")
print("Your percentage is "+str(int(score/7*100))+"%")
# show the final result when quiz is completed 