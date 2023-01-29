def is_leap_year(year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('Leap year')
            else: 
                print("Leap Year")
        else :
            print("Leap year")
    else:
        print("Not a leap year.")

year = int(input("Year : "))

is_leap_year(year)