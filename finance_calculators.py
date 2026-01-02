# Psudeocode:
# Request user input on what calculation_type is to be conducted - e.g. bond or investment
# Have two different blocks of code requesting relevant user inputs depending on calculation type
# Structure of each code block should take the following form:

    # 1. Request user inputs and define variables
    # 2. Calculate the total amount (bond - monthly repayement, investment - total return)
    # 3. Print amounts
    # 4. Add comment where input is not recognised

# Relevant pacakages imported
import math

# References
# Using multiple or conditions in python: https://stackoverflow.com/questions/17615020/what-is-the-best-approach-in-python-multiple-or-or-in-in-if-statement


print("Investment - to calculate the amount of interest you'll earn on your investment.\nBond - to calculate the amount you'll have to pay on a home loan\n")

calculation_type = input("Enter either “investment” or “bond” from the menu above to proceed: ")

# investment interest calculation

if calculation_type == "investment" or calculation_type == "Investment" or calculation_type == "INVESTMENT":
   
    # Step 1: Collect relevant inputs for calculating investment interest

    deposit = float(input("enter the amount of money to be deposited: "))
    interest_rate = float(input("Enter the interest rate (this must exclude the percentage sign): "))/100
    years = float(input("Enter the number of years you plan on investing: "))
    interest = input("Choose interest type (simple or compound): ")

    # Step 2.1: Calculate total investement amount (simple interest)

    if interest == "simple":
        total_amount = round(deposit 
                             * (1 + interest_rate * years))
        
    # Step 3.1: Print total investment amount (compound interest)

        print(f"The total interest earned with a {interest} interest rate of {interest_rate*100}% on a deposit of {deposit} over a {years} year period is ${total_amount}")
    
    # Step 2.2: Calculate total investement amount (compound)

    elif interest == "compound":
        total_amount = round(deposit 
                             * math.pow((1 + interest_rate),years))
        
    # Step 3.2: Print total investment value (compound interest)
        
        print(f"The total interest earned with a {interest} interest rate of {interest_rate*100}% on a deposit of {deposit} over a {years} period is ${total_amount}")
    
    # Notifies user that there is an error in the interest type selected

    else:
        print("User error. Please ensure one of the predefined options is selected and try again")

# Monthly bond repayment

elif calculation_type == "bond" or calculation_type == "Bond" or calculation_type == "BOND":

    # Step 1: Collect relevant inputs for calculating monthly bond repayments

    house_value = float(input("enter the present value of the property: "))
    interest_rate = float(input("Enter the interest rate (this must exclude the percentage sign): "))/100
    months = int(input("Enter the number of months you plan on repaying the bond: "))
    monthly_interest = interest_rate / 12

    # Step 2: Calculate bond repayement amount
    
    total_amount = round((monthly_interest * house_value)
                         /(1 - math.pow((1 + monthly_interest),(months*-1))))

    # Step 3: Print total monthly amount of bond repayment
    
    print(f"The monthly amount that needs to be repayed over {months} months with an interest rate of {interest_rate*100}% assuming a present value of ${house_value} is ${total_amount}")
    
# Final comment where user input is not identified
   
else:
    print("User error. Please ensure one of the predefined options is selected and try again")

