#collect email from use 
#split the email using @, use the first part as user name, saaved as domain 
#split domain using ' . '
from test import Emails

def main():
    print("Welcome to the email slicer !!!")
    print("  ")
    
    email_input = input("Enter your email : ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("username : ", username)
    print("domain: ", domain)
    print("extension : ", extension)

while True:
    main()
    print("")