# Define the principal amount (initial investment).
amt = 10000
# Define the annual interest rate as a percentage.
int = 3.5
# Define the number of years.
years = 7
# Calculate the future value of the investment using the compound interest formula.
future_value = amt * ((1 + (0.01 * int)) ** years)
# Round the future value to two decimal places and print it.
print(round(future_value, 2))
