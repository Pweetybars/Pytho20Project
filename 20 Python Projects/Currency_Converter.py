def main():
    print("This programm convert US Dollars to Khmer Riel")
    print()

    dollars  = eval(input("Enter amount in dollars: "))

    riels = convert_to_riels(dollars)

    print("That is ", riels, "KH Riels.")

convert_to_riels = lambda dollars : dollars * 4000

main()