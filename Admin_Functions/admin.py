'''Student ID: NP069619, NP069599, NP069604'''

import sys
import os
path=os.getcwd().replace("\\","\\\\")
sys.path.insert(0, f"{path}")
from Main_Functions.additionalfunctions import *

# Define the folder name
folder_name = 'Data'

# Create the directory if it doesn't exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Define file paths inside the new folder
LECTURERS_FILE = os.path.join(folder_name, 'lecturers.txt')
PERSONNEL_FILE = os.path.join(folder_name, 'personnel.txt')
SUBJECTS_FILE = os.path.join(folder_name, 'subjects.txt')

# Admin login credentials
admin_username = "1"
admin_password = "1"


def admin_login():
    """Handle admin login attempts."""
    attempts = 0
    while attempts < 3:
        username = input("Enter username: ").strip().lower()
        password = input("Enter password: ")
        clear()
        if username == admin_username and password == admin_password:
            print("\nLogin successful!")
            hold()
            clear()
            return True
        else:
            attempts += 1
            print("\nIncorrect credentials. Try again.\n")
            hold()
            clear()
    print('Maximum attempts reached. Access denied.')
    return False


def greet_admin():
    display()
    print("|                    Welcome Admin                    |")
    display()


def read_details(File_Name):
    """Read lecturers from the .txt file."""
    Details = []
    try:
        with open(File_Name, 'r') as file:
            for line in file:
                # creates dictionary within the list
                Details.append(eval(line.strip()))
    except FileNotFoundError:
        print("New file created")
    return Details


def write_details(FileName, Details):
    """Write lecturers and personnel to the .txt file."""
    with open(FileName, 'w') as file:
        for data in Details:
            file.write(f"{data}\n")  # Creates string of dictionary

def get_valid_name(prompt):
    while True:
        name = get_non_empty_input(prompt)
        if all(char.isalpha() or char.isspace() for char in name):
            return name
        print("Invalid name. Only alphabetic characters and spaces are allowed.")


def add_lecturer():
    """Add a new lecturer and save to the .txt file."""
    choice = 'y'
    while choice != 'n':
        lecturers = read_details(LECTURERS_FILE)
        lecturer = {
            'Username': get_non_empty_input("Enter lecturer username: "),
            'Password': get_strong_password(),
            'Name': get_valid_name("Enter lecturer name: "),
            'Address': get_non_empty_input("Enter lecturer address: "),
            'Contact Number': get_phone_number(),
            'DOB': get_date_of_birth(),
            'Email': get_email(),
            'Citizenship': get_citizenship(),
            'ID': generate_id(lecturers)  # Auto-generate ID
        }
        lecturer['Age'] = calculate_age(lecturer['DOB'])
        lecturers.append(lecturer)
        write_details(LECTURERS_FILE, lecturers)
        print("Lecturer added successfully.")

        # Ask if user wants to add another lecturer
        choice = input(
            "Do you want to add another lecturer? (y/n): ").strip().lower()

        # Clear screen for the next entry
        hold()
        clear()


def update_details(FileName):
    """Update Information."""
    details = read_details(FileName)
    if details == []:
        print("No details found to update.")
        return
    choice = 'y'
    while choice != 'n':
        view_details(FileName)
        username = get_non_empty_input("Enter username: ")
        found = False

        for data in details:
            if data['Username'] == username:
                data['Name'] = get_valid_name("Enter new name: ")
                data['Address'] = get_non_empty_input("Enter new address: ")
                data['Contact Number'] = get_phone_number()
                data['DOB'] = get_date_of_birth()
                data['Email'] = get_email()
                data['Age'] = calculate_age(data['DOB'])
                data['Citizenship'] = get_citizenship()
                write_details(FileName, details)
                print("Information updated successfully.")
                found = True
                break

        if not found:
            print("Username not found.")

        # Ask if user wants to update another record
        choice = input("Do you want to update another record? (y/n): ").strip().lower()

        # Clear screen for the next update
        hold()
        clear()


def delete_details(File_Name):
    """Delete a lecturer or a personnel by username."""
    Details = read_details(File_Name)
    if Details == []:
        return
    choice = 'y'
    while choice != 'n':
        view_details(File_Name)
        username = get_non_empty_input("Enter username: ")
        found = False
        for data in Details:
            if data['Username'] == username:
                Details = [
                    data for data in Details if data['Username'] != username]
                print("User deleted successfully.")
                write_details(File_Name, Details)
                found = True
                break
        if not found:
            print("Username not found.")
        # Ask if user wants to update another record
        choice = input(
            "Do you want to delete another record? (y/n): ").strip().lower()
        hold()
        clear()


def view_details(FileName):
    """View all lecturers or personnel."""
    Details = read_details(FileName)

    # Check if there are any details to display
    if Details:
        # Initialize headers and column widths
        headers = Details[0].keys()
        column_widths = {header: max(len(header), max(
            len(str(row[header])) for row in Details)) for header in headers}

        # Initialize table as an empty list
        table = []

        # Create header row
        header_row = " | ".join(
            [f"{header:<{column_widths[header]}}" for header in headers])
        table.append(header_row)

        # Create separator row
        separator_row = "-+-".join(['-' * column_widths[header]
                                   for header in headers])
        table.append(separator_row)

        # Create data rows using a loop
        for row in Details:
            data_row = " | ".join([f"{('*******' if header == 'Password' else str(
                row[header])):<{column_widths[header]}}" for header in headers])
            table.append(data_row)

        print("\n                                          Details Table                                      \n")
        # Print the table
        for line in table:
            print(line)
        print("\n")
    else:
        print("No details to show.\n")


def add_personnel():
    """Add a new personal entry and save to the .txt file."""
    personnel_data = read_details(PERSONNEL_FILE)
    choice = 'y'
    while choice != 'n':
        personnel = {
            'Username': get_non_empty_input("Enter personnel username: "),
            'Password': get_strong_password(),
            'Name': get_valid_name("Enter personnel name: "),
            'Address': get_non_empty_input("Enter personnel address: "),
            'Contact Number': get_phone_number(),
            'DOB': get_date_of_birth(),
            'Email': get_email(),
            'Citizenship': get_citizenship(),
            'ID': generate_id(personnel_data)  # Auto-generate ID
        }
        personnel['Age'] = calculate_age(personnel['DOB'])
        personnel_data.append(personnel)
        write_details(PERSONNEL_FILE, personnel_data)
        print("Personnel added successfully.")

        # Ask if user wants to add another lecturer
        # Get user input
        choice = input(
            "Do you want to add another personnel? (y/n): ").strip().lower()

        # Clear screen for the next entry
        hold()
        clear()


def add_subjects(File_Name):
    """Add new subjects and topics and save to the .txt file."""
    subjects = read_details(File_Name)
    choice = 'y'
    while choice != 'n':
        subject = {
            'Subject': get_non_empty_input("Enter subject: "),
            'Topics': get_non_empty_input("Enter topic: "),
        }

        # Check if the combination of subject and topics already exists
        if any(subj['Subject'].lower() == subject['Subject'].lower() and subj['Topics'].lower() == subject['Topics'].lower() for subj in subjects):
            print(
                "Subject and topic combination already exists. Please enter a different combination.")
            continue

        subjects.append(subject)

        # Ask if user wants to add more subjects
        choice = input(
            "Do you want to add more subjects and topics? (y/n): ").strip().lower()

    write_details(File_Name, subjects)
    print("Subjects and topics added successfully.")
    hold()
    clear()


def view_subject_topics(FileName):
    """View all subjects and topics."""
    subject_topics = read_details(FileName)
    if not subject_topics:
        print("No details to view.")
    else:
        print(f"{"Subjects"}\t\t{"Topics"}")
        print("-"*35)
        for data in subject_topics:
            print(f"""{(data['Subject']).capitalize()}\t\t\t{
                  (data['Topics']).capitalize()}""")


def admin_menu():
    """Main menu for academic administration."""
    if admin_login():
        while True:
            greet_admin()
            print(
                "\n1. Add Lecturer\n2. Update Lecturer\n3. Delete Lecturer\n4. View Lecturer\n5. Add Personnel\n6. Update Personnel\n7. Delete Personnel\n8. View Personnel\n9. Add Subjects and topics\n10. View Subject Details\n11. Logout\n")
            admin_choice = input("Enter choice: ")
            clear()
            if admin_choice == '1':
                add_lecturer()
            elif admin_choice == '2':
                update_details(LECTURERS_FILE)
            elif admin_choice == '3':
                delete_details(LECTURERS_FILE)
            elif admin_choice == '4':
                view_details(LECTURERS_FILE)
                hold()
                clear()
            elif admin_choice == '5':
                add_personnel()
            elif admin_choice == '6':
                update_details(PERSONNEL_FILE)
            elif admin_choice == '7':
                delete_details(PERSONNEL_FILE)
            elif admin_choice == '8':
                view_details(PERSONNEL_FILE)
                hold()
                clear()
            elif admin_choice == '9':
                add_subjects(SUBJECTS_FILE)
            elif admin_choice == '10':
                view_subject_topics(SUBJECTS_FILE)
                hold()
                clear()
            elif admin_choice == '11':
                break
            else:
                print("Invalid choice. Please try again.")
                hold()
                clear()
    else:
        print("Exiting due to failed login attempts.")


if __name__ == "__main__":
    admin_menu()
