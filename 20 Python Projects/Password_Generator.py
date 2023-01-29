# ASk user if they want to generate a password or not 
# If yes, ask for password 
# Generate Password 
# Print the password 
# if initial respond is No -> exit 

import string 
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("Length of your password : "))
    
    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you want to generate password? Yes/No ")


if option == "Yes":
    generate_password()
elif option == "No":
    print('Programm Ended')
    quit()
else: 
    print("Invalid")
    quit() 