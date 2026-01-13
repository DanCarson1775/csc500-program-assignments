"""
Part 1 - Meal Tip and Tax Calculator Program.

Calculates the total amount of a meal purchased at a resturant.

User is prompted for charge of the meal and calculations are performed using given constants. Results printed out ot user.
"""

print("Welcome to the Meal Tip, Tax, and Total Price Calculator Program!")

# Prompt user for meal charge
meal_charge = float(input("Enter meal charge amount: $"))

# Constants
TIP_RATE = 0.18
TAX_RATE = 0.07

# Calculate tip amount, tax amount, and total price
tip_amount = meal_charge * TIP_RATE
tax_amount = meal_charge * TAX_RATE
total_price = meal_charge + tip_amount + tax_amount

# Display output to user (terminal)
print(f"Tip Amount: ${tip_amount:,.2f}")
print(f"Tax Amount: ${tax_amount:,.2f}")
print(f"Total Price: ${total_price:,.2f}")
