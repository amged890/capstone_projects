# This code is a financial calculator for investments and home loan repayments . We ask the user
# what they want, and we proceed according to their choice. If they choose investments we ask them for the initial
# amount, time in years, rate per year and investment type. If they choose bond we ask about the house value,
# rate per year and time in months and return the amount they should pay each month.

import math
import matplotlib.pyplot as plt
while True:
    print("investment    - to calculate the amount of interest you'll earn on your investment.")
    print("bond          - to calculate the amount you'll have to pay on a home loan.")

    calculator_type = (input("Enter either 'investment' or 'bond' from the menu above to proceed:  ")).lower()

    if calculator_type == "cancel":
        print("Exiting program...")
        exit()


    elif calculator_type == "investment":
        deposit = int(input("Enter the amount of money you're depositing: "))
        interest_rate = (float(input("Enter the interest rate per year: %"))) / 100
        time_years = int(input("Enter the number of years you plan to invest: "))
        interest = (input("There's two interest types 'simple' and 'compound'. Enter the type you want: ")).lower()

        if interest == "cancel":
            print("Exiting program...")
            exit()


        elif interest == "simple":
            total_amount = [deposit * (1 + interest_rate * year) for year in range(1, time_years + 1)]
            print(f"The total amount you will get is {total_amount[-1]}£.")

        elif interest == "compound":
            total_amount = [deposit * math.pow((1 + interest_rate), year) for year in range(1, time_years + 1)]
            print(f"The total amount you will get is {total_amount[-1]}£.")

        else:
            print("Wrong input, please try again!")

        # Generate years for plotting
        years = list(range(1, time_years + 1))

        # Plot the investment growth
        plt.plot(years, total_amount)
        plt.title("Investment Growth Over Time")
        plt.xlabel("Years")
        plt.ylabel("Total Amount (£)")
        plt.grid(True)
        plt.show()


    elif calculator_type == "bond":
        house_value = int(input("Enter the present value of the house: "))
        monthly_interest_rate = (float(input("Enter the interest rate per year: %"))) / 1200
        time_month = int(input("Enter the number of months you plan to take to repay the bond: "))

        if house_value == "cancel" or monthly_interest_rate == "cancel" or time_month == "cancel":
            print("Exiting program...")
            exit()

        repayment = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate)**(-time_month))
        print(f"The amount you have to repay each month is {repayment}£.")


    else:
        print("Sorry, please try again with a valid choice from the menu.")

    repeat = input("Do you want to perform another calculation? (yes/no): ").lower()
    if repeat != "yes":
        break
