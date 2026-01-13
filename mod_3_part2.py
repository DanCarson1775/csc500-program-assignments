"""
Part 2 - Alarm Clock Program.

Calculates the time an alarm will go off based on a 24-hour clock.

User is prompted for current time and number of hours to wait. Future time is calculated and printed out to user.
"""

print("Welcome to the Alarm Clock Program!")

# Prompt for current time and hours to wait
current_time = int(input("What is the current time (0 - 23): "))
hours_to_wait = int(input("How long would you like ot wait: "))

# Validate that current time is acceptable input
if not (0 <= current_time <= 23):
    print("Invalid value. Enter number b/w 0 and 23. Please run program again.")

# Calculate total hours using a reference point
total_hours = current_time + hours_to_wait

# Remainder of whole number time is added to total hours calculated
alarm_trigger = total_hours % 24

# Output
print(f"Alarm will go off at {alarm_trigger}")
