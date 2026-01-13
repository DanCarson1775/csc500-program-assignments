"""Part 1 - Module adds and subtracts two numbers provided by the user."""

# Welcome message
print("Welcome! Please input two numbers to add and subtract.")

# User input
print("Enter first number: ", end="")
num1 = float(input())
print("Enter second number: ", end="")
num2 = float(input())

# Calculations
total_add = num1 + num2
total_sub = num1 - num2

# Results
print(f"{num1} + {num2} = {total_add}")
print(f"{num1} - {num2} = {total_sub}")
