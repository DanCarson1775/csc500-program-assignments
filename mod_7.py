"""
Module 7 - Criticial Thinking Assignment
CSU Course Information Lookup

Three dictionaries are created where each shares the same key but different values.
The user will enter a course number and the program will display information related to that course.
"""


room_numbers = {
    'CSC101': '3004',
    'CSC102': '4501',
    'CSC103': '6755',
    'NET110': '1244',
    'COM241': '1411'
}

instructors = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

meeting_times = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

# Prompt the user to enter a course number
course_number = input("Enter a course number (e.g., CSC102, NET110): ").upper()

# Check if the course number exists in the dictionaries
if course_number in room_numbers:
    # Retrieve and display the course's room number, instructor, and meeting time
    room = room_numbers[course_number]
    instructor = instructors[course_number]
    time = meeting_times[course_number]

    print(f"\nCourse Information for {course_number}:")
    print(f"Room Number: {room}")
    print(f"Instructor: {instructor}")
    print(f"Meeting Time: {time}")
else:
    # Display an error message if the course number is not found
    print(f"\nError: Course number '{course_number}' not found.")