# collect the necessary input : principal, rates, years of loan 
# calculate the monthly payment 
# show that to the suer 

def Rate_Calculator():
    print("This is a monthly payments loan calculator !!!") 
    print("       ")

    principal = float(input("Input the loan amount : ") ) 
    apr = float(input("The annual interest rate : "))
    years = int(input("Amount of years : "))

    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) **(-amount_of_months)) 

    print("The monthly payment is : %.2f " % (monthly_payment))

Rate_Calculator()   