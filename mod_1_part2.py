"""Part 2 - Module multiplies and divides two numbers provided by the user."""

# Welcome message
print("Welcome! Please input two numbers to multiply and divide.")

# User input
print("Enter first number: ", end="")
num1 = float(input())
print("Enter second number: ", end="")
num2 = float(input())

# Calculations
total_mul = num1 * num2
total_div = num1 / num2

# Results
print(f"{num1} x {num2} = {total_mul}")
print(f"{num1} / {num2} = {total_div}")
