"""
Module 5 - Criticial Thinking Assignment
Part 2 - CSU Global Bookstore Program

Points are awarded based on the number of books the user has purchased.
User is prompted for number of books purchase and a if/elif block is executed and points are distributed.
"""


def point_calc(num_books):
    """Determine number of points awarded based on number of books bought."""

    points = 0
    if num_books == 0:
        points = 0
    elif num_books == 2 or num_books == 3:
        points = 5
    elif num_books == 4 or num_books == 5:
        points = 15
    elif num_books == 6 or num_books == 7:
        points = 30
    elif num_books >= 8:
        points = 60
    else:
        points = 0
    return points


"""Main - Entry Point"""
if __name__ == "__main__":
    
    # Prompt number of books purchased
    num_books = int(input("Welcome to the CSU Global Bookstore\nHow many books did you purchase this month? "))

    # Function call
    awarded_points = point_calc(num_books)

    # Output
    print(f"You have been awarded {awarded_points} points.")
