# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   LRobinson,11/13/2023,Created Script
# ------------------------------------------------------------------------------------------ #


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: list = []  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# Create Enrollments csv to be read later.
file = open(FILE_NAME, "a+")
file.close()

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:   # Addressing the file not found error
    file = open(FILE_NAME, "r")
    for row in file.readlines():
        # Transform the data from the file
        student_data = row.split(',')
        student_data = [student_data[0], student_data[1], student_data[2].strip()]
        # Load it into our collection (list of lists)
        students.append(student_data)
    file.close()
except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if any(char.isdigit() for char in student_first_name):
                raise ValueError("The first name should only contain letters and special characters. ")

            student_last_name = input("Enter the student's last name: ")
            if any(char.isdigit() for char in student_last_name):
                raise ValueError("The last name should only contain letters. ")

            course_name = input("Please enter the name of the course: ")
            student_data = [student_first_name,student_last_name,course_name]
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            continue
        except ValueError as e:
            print(e)
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student[0]} {student[1]} is enrolled in {student[2]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:  # The program provides structured error handling when the dictionary rows are written to the file.
            file = open(FILE_NAME, "a")
            for student in students:
                csv_data = f"{student[0]},{student[1]},{student[2]}\n"
                file.write(csv_data)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student[0]} {student[1]} is enrolled in {student[2]}")
            continue
        except TypeError as e:
            print("Please check that the data is a valid csv format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.closed == False:
                file.close()


    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")

