# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   VarunParam,11/11/2024,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #
import json

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
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# Read all the data from Json file and load it   to a collection
file = open(FILE_NAME,"r")
students = json.load(file)
#for items in students:
    # for each data row read from json need to be loaded

    #student_data = {"FirstName": items['FirstName'],"LastName": student_data['LastName'],"CourseName": student_data['CourseName']}
    #students.append(student_data)
file.close()


# ------------------------------------------------------------------------------------------ #
# On menu choice 1, the program prompts the user to enter the student's first name and  last name,
# followed by the course name, using the input() function and stores the inputs in the respective variables.
# ------------------------------------------------------------------------------------------ #

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)

    # Input user data
    menu_choice = input("What would you like to do: ")

    # Using case statements, instead of If, as If statement runs through each and every loop
    # Confirmed the Use of match case Statements from Randal, instead of if else
    match menu_choice:
        case "1":
            student_first_name = input('Enter Student\'s First Name: ')
            student_last_name= input('Enter Student\'s Last Name: ')
            course_name= input('Enter Course Name: ')
            # Checking for the string variables or not empty
            if student_first_name!= "" and student_last_name!= "" and student_last_name != "":
                # Creates a dictionary object
                student_data = {"FirstName": student_first_name,"LastName": student_last_name,"CourseName": course_name}
                # Appending the record to students List
                students.append(student_data)
            else:
                # if all the data is not present then print below message
                print("No data to Record. Please enter Student details.")

 # Present the current data
        case "2":
            # ------------------------------------------------------------------------------------------ #
            # •	On menu choice 2, the presents a string by formatting the collected data using the print() function.
            # •	Data collected for menu choice 1 is added to a two-dimensional list table (list of dictionaries).
            # •	All data in the list is displayed when menu choice 2 is used.
            # ------------------------------------------------------------------------------------------ #

            if len(students) > 0:
                for student in students:
                    # csv_data is holding data in format "student_first_name,student_last_name,course_name"
                    csv_data = f"{student["FirstName"]}, {student["LastName"]}, {student["CourseName"]}"
                    print(csv_data)
            else:
                # if all the data is not present then print below message
                print("No students records . Please enter Student details.")

    # Save the data to a file
        case "3":
            if len(students) > 0:
                file: object = open(FILE_NAME, "w")
                json.dump(students, file)
                for student in students:
                    # csv_data is holding data in format "student_first_name,student_last_name,course_name"
                    csv_data = f"{student["FirstName"]}, {student["LastName"]}, {student["CourseName"]}"
                    print(csv_data)
                file.close()


            else:
                # if all the data is not present then print below message
                print("No data to save . Please enter Student details.")
    # Stop the loop
        case "4":
            print("Exiting Program...")
            break
        case other:
            print("Choose a valid option from the menu.")