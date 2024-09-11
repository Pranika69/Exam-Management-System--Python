'''Student ID: NP069604,NP069599'''

import sys
import os
path=os.getcwd().replace("\\","\\\\")
sys.path.insert(0, f"{path}")
from Main_Functions.additionalfunctions import *
from Admin_Functions.admin import *

# Define the folder name
folder_name = 'Data'

# Create the directory if it doesn't exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Define file paths inside the new folder
LECTURERS_FILE = os.path.join(folder_name, 'lecturers.txt')
SUBJECTS_FILE = os.path.join(folder_name, 'subjects.txt')

def greetlecturer():
    display()
    print("|                   Welcome Leturer                   |")
    display()


def add_questions(FileName):
    """Add questions and save to the .txt file."""
    subjects = read_details(FileName)
    repeat = 'y'
    subject = get_non_empty_input("Enter subject: ")
    topic = get_non_empty_input("Enter topic: ")
    for data in subjects:
        # checks entered topic and subject
        if data['Subject'] == subject and data['Topics'] == topic:
            while repeat != 'n':
                hold()
                clear()
                print("\nQuestions")
                print("1. Multiple-choice\n2. Subjective")
                question_type = input("\nEnter your choice: ")
                if question_type == '1':
                    choice_mcq = 'y'
                    while choice_mcq != 'n':
                        mcq_question = get_non_empty_input(
                            "\nEnter question: ")
                        mcq_answer = get_non_empty_input("\nEnter answer: ")
                        if 'MCQ' in data:
                            data['MCQ'].append(mcq_question)
                        else:
                            data['MCQ'] = [mcq_question]

                        if 'MCA' in data:
                            data['MCA'].append(mcq_answer)
                        else:
                            data['MCA'] = [mcq_answer]
                        if len(data['MCQ']) >= 5:
                            choice_mcq = get_non_empty_input("\nDo you want to add more mcqs?(yes-y/no-n): ")
        
                    write_details(FileName, subjects)
                    print("\nMultiple Choice Questions added successfully. ")

                elif question_type == '2':
                    choice_subjective = 'y'
                    while choice_subjective != 'n':
                        subjective_question = get_non_empty_input(
                            "\nEnter question: ")
                        subjective_answer = get_non_empty_input(
                            "\nEnter answer: ")
                        if 'SQ' in data:
                            data['SQ'].append(subjective_question)
                        else:
                            data['SQ'] = [subjective_question]

                        if 'SA' in data:
                            data['SA'].append(subjective_answer)
                        else:
                            data['SA'] = [subjective_answer]
                        if len(data['SQ']) >= 2:
                            choice_subjective = input("Do you want to add more subjective questions?(yes-y/no-n): ").strip().lower()
                    write_details(FileName, subjects)
                    print("\nSubjective Questions added successfully.")
                else:
                    print(
                        "Invalid input. Please enter '1' for Multiple-choice or '2' for Subjective.")
                    continue  # Restart the loop to re-prompt for question_type

                repeat = input(
                    "\nDo you want to add more questions(yes-y/no-n)? ").strip().lower()
            hold()
            clear()
            return
    print("Subject and topic not found.")
    hold()
    clear()


def update_questions(FileName):
    """Update Information."""
    questions = read_details(FileName)
    if questions == []:
        return
    else:
        subject = get_non_empty_input("Enter subject: ")
        topic = get_non_empty_input("Enter topic: ")
        for data in questions:
            if data['Subject'] == subject and data['Topics'] == topic:
                repeat = 'y'
                while repeat != 'n':
                    hold()
                    clear()
                    print("\nQuestions")
                    print("1. Multiple-choice\n2. Subjective")
                    question_type = input("\nEnter your choice: ")
                    if question_type == '1':
                        if 'MCQ' in data:
                            choice_mcq = 'y'
                            while choice_mcq != 'n':
                                hold()
                                clear()
                                view_mcq_questions(questions, subject, topic)
                                mcq_question_no = int(
                                    get_non_empty_input("Enter question number: "))

                                if mcq_question_no < 1 or mcq_question_no > len(data['MCQ']):
                                    print(
                                        "Invalid number. Please enter a valid question number.")
                                    continue

                                data['MCQ'][mcq_question_no -
                                            1] = input("Enter new question: ")
                                data['MCA'][mcq_question_no -
                                            1] = input("Enter new answer: ")
                                choice_mcq = get_non_empty_input("Do you want to update more mcqs? (y/n):")
                            write_details(FileName, questions)
                            print(
                                "\nMultiple Choice Questions updated successfully.")
                        else:
                            print("No details to update.")
                    elif question_type == '2':
                        if 'SQ' in data:
                            choice_subjective = 'y'
                            while choice_subjective != 'n':
                                hold()
                                clear()
                                view_subjective_questions(
                                    questions, subject, topic)
                                su_question_no = int(
                                    get_non_empty_input("Enter question number: "))

                                if su_question_no < 1 or su_question_no > len(data['SQ']):
                                    print(
                                        "Invalid number. Please enter a valid question number.")
                                    continue

                                data['SQ'][su_question_no -
                                           1] = input("Enter new question: ")
                                data['SA'][su_question_no -
                                           1] = input("Enter new answer: ")
                                choice_subjective = get_non_empty_input(
                                    "\nDo you want to update more subjective questions? (yes-y/no-n): ").strip().lower()

                            write_details(FileName, questions)
                            print("\nSubjective Questions updated successfully.")
                        else:
                            print("No details to update.")
                    else:
                        print(
                            "Invalid input. Please enter '1' for Multiple-choice or '2' for Subjective.")
                        hold()
                        clear()
                        continue  # Restart the loop to re-prompt for question_type
                    # Get user input
                    repeat = input(
                        "\nDo you want to update more questions? (yes-y/no-n): ").strip().lower()
                hold()
                clear()
                return
        print("Subject and topic not found.")
        hold()
        clear()


def view_mcq_questions(data, subject, topic):
    """View all MCQ and MCA questions and answers."""
    for entry in data:
        if entry['Subject'] == subject and entry['Topics'] == topic:
            print(f"{'='*50}")
            print(f"Subject: {entry['Subject']} | Topic: {entry['Topics']}")
            print(f"{'-'*50}")

            if 'MCQ' in entry and entry['MCQ']:
                print("\nMultiple Choice Questions (MCQ):")
                for i in range(len(entry['MCQ'])):
                    print(f"  Q{i+1}: {entry['MCQ'][i]}")

            if 'MCA' in entry and entry['MCA']:
                print("\nMultiple Choice Answers (MCA):")
                for i in range(len(entry['MCA'])):
                    print(f"  A{i+1}: {entry['MCA'][i]}")
            print(f"{'='*50}\n")


def view_subjective_questions(data, subject, topic):
    """View all SQ and SA questions and answers."""
    for entry in data:
        if entry['Subject'] == subject and entry['Topics'] == topic:
            print(f"{'='*50}")
            print(f"Subject: {entry['Subject']} | Topic: {entry['Topics']}")
            print(f"{'-'*50}")

            if 'SQ' in entry and entry['SQ']:
                print("\nShort Questions (SQ):")
                for i in range(len(entry['SQ'])):
                    print(f"  Q{i+1}: {entry['SQ'][i]}")

            if 'SA' in entry and entry['SA']:
                print("\nShort Answers (SA):")
                for i in range(len(entry['SA'])):
                    print(f"  A{i+1}: {entry['SA'][i]}")
            print(f"{'='*50}\n")


def view_questions(FileName):
    """Ask the user which type of questions they want to view and call the appropriate function."""
    subject_topics = read_details(FileName)
    if not subject_topics:
        print("No details to view.")
        hold()
        clear()
    else:
        subject = get_non_empty_input("Enter subject: ")
        topic = get_non_empty_input("Enter topic: ")
        for data in subject_topics:
            if data['Subject'] == subject and data['Topics'] == topic:
                repeat = 'y'
                while repeat != 'n':
                    hold()
                    clear()
                    print("\nView Questions\n1. MCQ Questions\n2. Subjective Questions\n3. Both")
                    choice = input("\nEnter your choice: ")
                    clear()
                    if choice == '1':
                        view_mcq_questions(subject_topics, subject, topic)
                    elif choice == '2':
                        view_subjective_questions(subject_topics, subject, topic)
                    elif choice == '3':
                        view_mcq_questions(subject_topics, subject, topic)
                        view_subjective_questions(subject_topics, subject, topic)
                    else:
                        print("Invalid choice. Please enter valid choice.")
                        clear()
                        continue
                    # Get user input
                    repeat = input("\nDo you want to view again? (yes-y/no-n): ").strip().lower()
                hold()
                clear()      
                return
        print("Subject and topic not found.")
        hold()
        clear()

def validate_login(fileName):
    """Handle personnel login attempts."""
    attempts = 0
    Details = read_details(fileName)
    while attempts < 3:
        username = input("Enter username: ")
        password = input("Enter password: ")
        clear()
        for data in Details:
            if data['Username'] == username and data['Password'] == password:
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


def update_credentials(FileName):
    """Update Information."""
    details = read_details(FileName)
    if details == []:
        return
    else:
        username = get_non_empty_input("Enter username: ")
        for data in details:
            if data['Username'] == username:
                data['Username'] = get_non_empty_input("Enter new username: ")
                data['Password'] = get_strong_password()
                write_details(FileName, details)
                print("Information updated successfully.")
                hold()
                clear()
                return
        print("Username not found.")
        hold()
        clear()


def lecturer_menu():
    """Main menu for academic administration."""
    if validate_login(LECTURERS_FILE):
        while True:
            greetlecturer()
            print("\n1. Change Username and Password\n2. Add Question\n3. Update Question\n4. View Questions\n5. Logout\n")
            lecturer_choice = input("Enter choice: ")
            clear()
            if lecturer_choice == '1':
                update_credentials(LECTURERS_FILE)
            elif lecturer_choice == '2':
                view_subject_topics(SUBJECTS_FILE)
                add_questions(SUBJECTS_FILE)
            elif lecturer_choice == '3':
                view_subject_topics(SUBJECTS_FILE)
                update_questions(SUBJECTS_FILE)
            elif lecturer_choice == '4':
                view_subject_topics(SUBJECTS_FILE)
                view_questions(SUBJECTS_FILE)
            elif lecturer_choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")
                hold()
                clear()
    else:
        print("Exiting due to failed login attempts.")


if __name__ == "__main__":
    lecturer_menu()
