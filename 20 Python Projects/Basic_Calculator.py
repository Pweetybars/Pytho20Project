#defind a function needed to add sub mul div
#print option to the user * + - /
#prompt the user for the values 
#call the function 
#while loop to continue  until the user want to exit 

def add(a, b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer))

def sub(a, b):
    answer = a - b 
    print(str(a) + "-" + str(b) + " = "+ str(answer))

def mul(a, b):
    answer = a * b 
    print(str(a) + "*" + str(b) + " = "+ str(answer))

def div(a, b):
    answer = a / b 
    print(str(a) + "/" + str(b) + " = "+ str(answer))

while True :
    print("A. Addition ")
    print("B. Substraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Enter your choice : ")


    if choice == 'A' or choice == 'a':
        print("Addition")
        a = int(input("Your first number : "))
        b = int(input("Your Second number : "))
        add(a , b)
    elif choice == 'B' or choice == 'b':
        print("Substraction")
        a = int(input("Your first number : "))
        b = int(input("Your Second number : "))
        sub(a, b)
    elif choice == 'C' or choice == 'c': 
        print("Multiplication")
        a = int(input("Your first number : "))
        b = int(input("Your Second number : "))
        mul(a, b)
    elif choice == 'D' or choice == 'd':
        print("Division")
        a = int(input("Your first number : "))
        b = int(input("Your Second number : "))
        div(a, b)
    elif choice == 'E' or choice == 'e':
        print("Program Ended")
        quit()