# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions,
# Classes and using the separation of concerns Pattern
# with structured error handling
# Change Log: (Who, When, What)
#   Varun reddy Param, 11/19/2024,Created Script
#   <Your Name Here>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #

import json
import io as _io

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
#declared Constant to hold the Json file
FILE_NAME: str = "Enrollments.json"
#Declaring Variables to reuse and hold the data
student_table: list = []
menu_choice = ''

class FileProcessor:
    """
    A collection of variables and functions that can Process the data to get the file info

    ChangeLog: (Who, When, What)
    Varun Reddy Param,11.19.2024,Created Class
    """

    # ------------------------------------------------------------------------------------------ #
    #  When the program starts,
    #  the contents of the "Enrollments.json" are automatically read into a two-dimensional list table (a list of dictionary rows).
    #  (Tip: Make sure to put some starting data into the file or you will get an error!)
    # ------------------------------------------------------------------------------------------ #

    # Read all the data from Json file and load it   to a collection
    @staticmethod 
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file into a list of dictionary rows

        Notes:
        - Data sent to the student_data parameter will be overwritten.

        ChangeLog: (Who, When, What)
        Varun reddy Param,11.19.2024, Created function

        :param file_name: string with the name of the file we are reading
        :param student_data: list of dictionary rows we are adding data to
        :return: list of dictionary rows filled with data
        """

        try:
            file = open(file_name,"r")
            student_data = json.load(file)
            IO.output_student_courses(student_data)

        except FileNotFoundError as e:
            IO.output_error_messages("file must exist before running this script!", e)
        
        except Exception as e:
            IO.output_error_messages("There was a non-specific error when reading the file!", e)
        
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function reads data from a json file into a list of dictionary rows

        Notes:
        - Data sent to the student_data parameter will be overwritten.

        ChangeLog: (Who, When, What)
        Varun reddy Param,11.19.2024, Created function

        :param file_name: string with the name of the file we are writing to
        :param student_data: list of dictionary rows that contains data to
        :return: none
        """

        if len(student_data) > 0:
            try:
                file = open(file_name, "w")
                json.dump(student_data, file)
            except FileNotFoundError as e:
                IO.output_error_messages("file must exist before running this script!", e)
            except Exception as e:
                IO.output_error_messages("There was a non-specific error when reading the file!", e)
            finally:
                if file.closed == False:
                    file.close()
        else:
                # if all the data is not present then print below message
                print("No data to save . Please enter Student details.")


class IO:
    """
    A collection of functions that is used for input and outputs

    ChangeLog: (Who, When, What)
    Varun Reddy Param,11.19.2024,Created Class
    Varun Reddy Param,11.19.2024,Created a common function for printing the error Messages
    Varun Reddy Param,11.19.2024,Created a function to show the Menu
    Varun Reddy Param,11.19.2024,Created a function to take user inputs
    Varun Reddy Param,11.19.2024,Created a function to create data collection 
    """
    
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays custom error messages to the user

        ChangeLog: (Who, When, What)
        Varun reddy Param,11.19.2024, Created function

        :param message: string with the message to show
        :param error: type of error
        :return: none
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')
        
    @staticmethod
    def output_menu(menu: str):
        """ This function displays Menu options for the user

        ChangeLog: (Who, When, What)
        Varun reddy Param,11.19.2024, Created function
        
        :param menu: string with Menu options to show
        :return: none
        """
        print(menu,end='\n\n')

    @staticmethod    
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        Varun reddy Param,11.19.2024, Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("You must choose 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets data from the user and adds it to a list of dictionary rows

        ChangeLog: (Who, When, What)
        Varun reddy Param,11.19.2024, Created function

        :param student_data: list of dictionary rows containing our current data
        :return: list of dictionary rows filled with a new row of data
        """

        try:
            student_first_name = input('Enter Student\'s First Name: ')
             # Check if first name is a valid input
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers and empty.")
            student_last_name = input("Enter Student\'s Last Name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers and Empty.")
            course_name = input('Enter Course Name: ')
            # Checking if all the required fields are not empty
            if student_first_name.strip() and student_last_name.strip() and course_name.strip():
                # Creates a dictionary object
                student:dict = {"FirstName": student_first_name, "LastName": student_last_name,
                                "CourseName": course_name}
                # Appending the record to students list
                student_data.append(student)
                print("Student data recorded successfully.")
            else:
                # If all the data is not present then print the below message
                print("No data to record. Please enter complete student details.")

        except ValueError as e:
            IO.output_error_messages("Only use names without numbers", e)  # Prints the custom message
        except Exception as e:
            IO.output_error_messages("There was a non-specific error when adding data!", e)

        return student_data
    
    @staticmethod
    def output_student_courses(student_data: list):
        """ This function displays the current data to the user

        ChangeLog: (Who, When, What)
        Varun reddy Param,11.19.2024, Created function

        :return: None
        """

        if len(student_data) > 0:
            print('=' * 60)
            for student in student_data:
                # csv_data is holding data in format "student_first_name,student_last_name,course_name"
                csv_data: str = f"{student["FirstName"]}, {student["LastName"]}, {student["CourseName"]}"
                print(csv_data)
            print('=' * 60, end='\n\n')
        else:
            # if all the data is not present then print below message
            print("No students records . Please enter Student details.")


student_table = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=student_table)

# ------------------------------------------------------------------------------------------ #
# On menu choice 1, the program prompts the user to enter the student's first name and  last name,
# followed by the course name, using the input() function and stores the inputs in the respective variables.
# ------------------------------------------------------------------------------------------ #

# Present and Process the data
while True:

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    # Input user data
    menu_choice = IO.input_menu_choice()

    # Using case statements, instead of If, as If statement runs through each and every loop
    # Confirmed to Use of match case Statements from Randal, instead of if else
    match menu_choice:
        case "1":
            IO.input_student_data(student_data=student_table)

 # Present the current data
        case "2":
            # ------------------------------------------------------------------------------------------ #
            # •	On menu choice 2, the presents a string by formatting the collected data using the print() function.
            # •	Data collected for menu choice 1 is added to a two-dimensional list table (list of dictionaries).
            # •	All data in the list is displayed when menu choice 2 is used.
            # ------------------------------------------------------------------------------------------ #

            print("\n Here is the updated data")
            IO.output_student_courses(student_data=student_table)

    # Save the data to a file
        case "3":
            # ------------------------------------------------------------------------------------------ #
            # On menu choice 3, the program opens a file named "Enrollments.json" in write mode using the open() function.
            # It writes the content of the students variable to the file using the dump() function,
            # then file is closed using the close() method. Then displays what was stored in the file.
            # ------------------------------------------------------------------------------------------ #

            FileProcessor.write_data_to_file(file_name=FILE_NAME,student_data=student_table)
    # Stop the loop
        case "4":
            # ------------------------------------------------------------------------------------------ #
            # On menu choice 4, the program ends.
            # ------------------------------------------------------------------------------------------ #
            print("Exiting Program...")
            break
        case other:
            print("Choose a valid option from the menu.")
