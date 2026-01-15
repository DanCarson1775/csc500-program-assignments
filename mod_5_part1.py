"""
Module 5 - Criticial Thinking Assignment

<DESCRIBE PROGRAM>
"""


def calc_avg_rainfall(num_years):

    # Local scope variables
    total_rainfall = 0
    total_months = 0

    # Outer loop iterates once per year
    for year in range(1, num_years + 1):
        print(f"Year: {year}")

        # Inner loop iterates 12 times a year (12 x per year)
        for month in range(1, 13):
            # Prompt inches of rainfall
            inch_rainfall = float(input(f"How many inches of rainfall for month {month}? "))
            # Increase counters
            total_rainfall += inch_rainfall
            total_months += 1

    # Calc total rainfall average
    avg_total_rainfall = total_rainfall / total_months
    # Return tuple of values to main
    return total_rainfall, total_months, avg_total_rainfall


"""Main - Entry Point"""
if __name__ == "__main__":
    
    # Prompt number of years
    num_years = int(input("Welcome to the Average Rainfall Calculator\nHow many years of coverage would you like? "))

    # Function call
    total_rainfall, total_months, avg_total_rainfall = calc_avg_rainfall(num_years)

    # Output
    print(f"Total Number of Months: {total_months}")
    print(f"Total Inches of Rainfall: {total_rainfall:.2f}")
    print(f"Total Average Rainfall over Period: {avg_total_rainfall:.2f}")
