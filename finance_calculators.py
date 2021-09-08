# finance_calculators

# Problem:
"""creating a program that allows the user to calculate their interest on an investment or calculate the amount that should be
repaid on a home loan each month."""

import math

# asking user to choose type of calculation they would like
print("Choose either 'Investment' or 'Bond' from the menu below to begin: ")

user_response = input("Enter response here: ")

# Validating user_response and prompting relative/appropriate input
# Calculating for investiment
if user_response.lower() == 'investment':
    amount_being_deposited = float(input("Please enter amount of money you would like to deposit: "))
    interest_rate = int(input("Please enter the interest rate: "))
    years_of_investment = int(input("Please enter the number of years you plan on investing for: "))
    interest = input("Please confirm if you would like 'simple' or 'Compound' interest: ")

    actual_interest = (interest_rate / 100) # Given interest divided by 100

    if interest.lower() == 'simple': # Calculating for simple interest
        simple_amount = amount_being_deposited * (1 + (actual_interest * years_of_investment))
        simple_amount = round(simple_amount, 2)
        print(f"\nYou have selected simple interest, hence your total is R{simple_amount}")

    elif interest.lower() == 'compound': # Calculating for compound interest
        compound_amount = amount_being_deposited * math.pow((1 + actual_interest) , years_of_investment)
        compound_amount = round(compound_amount, 2)
        print(f"\nYou have selected compound interest, hence your total is R{compound_amount}")
    else:
            print("Invalid input!! Please try again")
        
#Calculating for bond
elif user_response.lower() == 'bond':
    present_value_of_house = float(input("Please enter the present value of the house: "))
    bond_interest_rate = int(input("Please enter the interest: "))
    months_to_repay = int(input("Please enter the number of months you will take to repay: "))

    monthly_interest_rate = ((bond_interest_rate / 100) / 12)
    grand_monthly_bond_amount = (present_value_of_house * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**(-months_to_repay))
    print(f"\nYour monthly payment amount will be: R{(float('%.2f'%(grand_monthly_bond_amount)))} ")

else:
    print("Invalid input!!! Please try again")

# Apologies, I realized my dropbox was not syncing causing changes not to reflect
