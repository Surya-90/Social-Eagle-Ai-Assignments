
# This program takes a student's mark as input and outputs the corresponding grade based on the following scale:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# E: 0-59
# Avoided using letters or special characters in the input.
# Avoided marks outside the range of 0-100.
# Avoided application unexpected crashes.


def GradeMarks():
    try:
        mark = input("Enter your mark (0-100): ")
        if not mark.isdigit():
            print("Please provide numbers only, not letters or special characters.")
            return
        
        mark = int(mark)

        if mark < 0 or mark > 100:
            print("Please enter a number between 0 and 100.")
            return
        
        if mark >= 90:
            grade = 'A'
        elif mark >= 80:
            grade = 'B'
        elif mark >= 70:
            grade = 'C'
        elif mark >= 60:
            grade = 'D'
        else:
            grade = 'E'
        print(f"Your grade is: {grade}")
    except Exception as e:
        print(f"Error: {e}")

GradeMarks()
