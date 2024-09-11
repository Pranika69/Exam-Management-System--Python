'''Student ID: NP069599'''

import sys
import os
path=os.getcwd().replace("\\","\\\\")
sys.path.insert(0, f"{path}")
from Lecturer_Functions.lecturer import *
from Admin_Functions.admin import *
from Main_Functions.additionalfunctions import *

# Define the folder name
folder_name = 'Data'

# Create the directory if it doesn't exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Define file paths inside the new folder
PERSONNEL_FILE = os.path.join(folder_name, 'personnel.txt')
SUBJECTS_FILE = os.path.join(folder_name, 'subjects.txt')
EXAM_FILE = os.path.join(folder_name,'exam_details.txt')

def display_examsets():
    exam_details = read_details(EXAM_FILE)
    if not exam_details:
        print("No details to view.")
        hold()
        clear()
    else:
        subject = get_non_empty_input("Enter subject: ")
        topic = get_non_empty_input("Enter topic: ")
        set_type = get_non_empty_input("Enter set: ")
        display_set_questions(exam_details, subject, topic, set_type)


def display_set_questions(exam_details, subject, topic, set_type):
    for details in exam_details:
        if details['Subject'] == subject and details['Topics'] == topic and details['Set'] == set_type:
                hold()
                clear()
                print(f"\nSet: {set_type.upper()}")
                print(f"Subject: {subject.capitalize()}")
                print(f"Topic: {topic.capitalize()}\n")

                if 'SectionA' in details:
                    print("Section A:")
                    idx = 1
                    for question in details['SectionA']:
                        print(f"{idx}. {question}")
                        idx += 1
                else:
                    print("Section A: No questions available.")

                print("\n")

                if 'SectionB' in details:
                    print("Section B:")
                    idx = 1
                    for question in details['SectionB']:
                        print(f"{idx}. {question}")
                        idx += 1
                else:
                    print("Section B: No questions available.") 
        return
    print("No set found for the specified subject and topic.")
    hold()
    clear()


def display_subject_topic_sets():
    exam_details = read_details(EXAM_FILE)
    if not exam_details:
        print("No details to view.")
        hold()
        clear()
    else:
        # Print table headers
        print(f"{"Subjects"}\t\t{"Topics"}\t\t{"Sets"}")
        print("-"*60)
        for data in exam_details:
            print(f"""{(data['Subject']).capitalize()}\t\t\t{
                  (data['Topics']).capitalize()}\t\t{data['Set'].upper()}""")


def modify_papers():
    # Function to modify the exam papers
    # The user will be asked to enter the subject name and the exam paper number to be modified
    # The user will be asked to enter the new exam paper details
    # The modified exam paper details will be written to the exam_details.txt file

    exam_details = read_details(EXAM_FILE)
    if exam_details == []:
        return
    else:
        subject = get_non_empty_input("Enter subject: ")
        topic = get_non_empty_input("Enter topic: ")
        set_type = get_non_empty_input("Enter set: ")
        for data in exam_details:
            if data['Subject'] == subject and data['Topics'] == topic and data['Set'] == set_type:
                repeat = 'y'
                while repeat != 'n':
                    hold()
                    clear()
                    print("\nChoose Section to update\n1. Section A\n2. Section B")
                    section = get_non_empty_input("Enter your choice: ")
                    if section == '1':
                        if 'SectionA' in data:
                            choice_mcq = 'y'
                            while choice_mcq != 'n':
                                display_set_questions(exam_details, subject, topic, set_type)
                                print("\nChoose question to update in Section A")
                                mcq_question_no = int(
                                    get_non_empty_input("\nEnter question number: "))

                                if mcq_question_no < 1 or mcq_question_no > len(data['SectionA']):
                                    print(
                                        "Invalid number. Please enter a valid question number.")
                                    continue

                                data['SectionA'][mcq_question_no -
                                                 1] = input("Enter new question: ")
                                choice_mcq = get_non_empty_input(
                                    "Do you want to update more question in Section A? (y/n): ")

                            write_details(EXAM_FILE, exam_details)
                            print("\nSectionA Questions updated successfully.")
                        else:
                            print("No details to update.")
                    elif section == '2':
                        if 'SectionB' in data:
                            choice_subjective = 'y'
                            while choice_subjective != 'n':
                                display_set_questions(exam_details, subject, topic, set_type)                              
                                print("\nChoose question to update in Section B")
                                su_question_no = int(
                                    get_non_empty_input("\nEnter question number: "))

                                if su_question_no < 1 or su_question_no > len(data['SectionB']):
                                    print(
                                        "Invalid number. Please enter a valid question number.")
                                    continue

                                data['SectionB'][su_question_no -
                                                 1] = input("Enter new question: ")
                                choice_subjective = input(
                                    "\nDo you want to update more question in Section B? (yes-y/no-n): ").strip().lower()

                            write_details(EXAM_FILE, exam_details)
                            print("\nSectionB Questions updated successfully.")
                        else:
                            print("No details to update.")
                    else:
                        print(
                            "Invalid input. Please enter '1' for Multiple-choice or '2' for Subjective.")
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


def add_questions(FileName):
    "Add questions(SectionA, SectionB) to the set"
    questions = read_details(FileName)
    exam_details = read_details(EXAM_FILE)
    subject = get_non_empty_input("Enter subject: ")
    topic = get_non_empty_input("Enter topic: ")
    set_type = get_non_empty_input("Enter set: ")

    for details in exam_details:
        if details['Subject'] == subject and details['Topics'] == topic and details['Set'] == set_type:
            for data in questions:
                if data['Subject'] == subject and data['Topics'] == topic:
                    sec_choice = 'y'
                    while sec_choice != 'n':
                        hold()
                        clear()
                        print(f"\n{set_type.upper()}")
                        print("\n1. SectionA\n2. SectionB")
                        section = get_non_empty_input("Enter your choice: ")
                        if section == '1':
                            if 'MCQ' in data:
                                choice_mcq = 'y'
                                while choice_mcq != 'n':
                                    hold()
                                    clear()
                                    view_mcq_questions(
                                        questions, subject, topic)
                                    mcq_question_no = int(
                                        get_non_empty_input("Enter question number: "))
                                    if mcq_question_no < 1 or mcq_question_no > len(data['MCQ']):
                                        print(
                                            "Invalid number. Please enter a valid question number.")
                                        continue
                                    mcq_question = data['MCQ'][mcq_question_no - 1]
                                    if 'SectionA' not in details:
                                        details['SectionA'] = []
                                    if mcq_question not in details['SectionA']:
                                        details['SectionA'].append(
                                            mcq_question)
                                    else:
                                        print(
                                            "Question already exists in Section A.")
                                    choice_mcq = get_non_empty_input(
                                        "Do you want to add more questions? (y/n): ")

                                write_details(EXAM_FILE, exam_details)
                                print(
                                    "\nMultiple Choice Questions added to Section A successfully.")
                                hold()
                                clear()
                            else:
                                print("\nNo MCQs to add.\n")
                        elif section == '2':
                            if 'SQ' in data:
                                choice_sq = 'y'
                                while choice_sq != 'n':
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
                                    su_question = data['SQ'][su_question_no - 1]
                                    if 'SectionB' not in details:
                                        details['SectionB'] = []
                                    if su_question not in details['SectionB']:
                                        details['SectionB'].append(su_question)
                                    else:
                                        print(
                                            "Question already exists in Section B.")
                                    choice_sq = get_non_empty_input(
                                        "Do you want to add more questions? (y/n): ")

                                write_details(EXAM_FILE, exam_details)
                                print(
                                    "\nSubjective Questions added to Section B successfully.")
                                hold()
                                clear()
                            else:
                                print("\nNo subjective questions to add.\n")
                        else:
                            print("\nInvalid Input. Please enter again.")
                            continue
                        sec_choice = get_non_empty_input(f"""Do you want to add more questions in {
                                                         set_type.upper()}(yes-y/no-n): """)
            hold()
            clear()
            return
    print("No set found for the subject and topic.")
    hold()
    clear()


def greetpersonnel():
    display()
    print("|              Welcome Exam Unit Personnel            |")
    display()


def create_sets(FileName):
    """Create new sets for the exam and save to the .txt file."""
    questions = read_details(FileName)
    subject = get_non_empty_input("Enter subject: ")
    topic = get_non_empty_input("Enter topic: ")
    for data in questions:
        if data['Subject'] == subject and data['Topics'] == topic:
            choice = 'y'
            exam_details = read_details(EXAM_FILE)
            while choice != 'n':
                set_questions = {
                    'Subject': data['Subject'],
                    'Topics': data['Topics'],
                    'Set': get_non_empty_input("Enter set name: "),
                }
                # Check if the combination of subject and topics and already exists
                if any(subj['Subject'].lower() == set_questions['Subject'].lower() and subj['Topics'].lower() == set_questions['Topics'].lower() and subj['Set'].lower() == set_questions['Set'].lower() for subj in exam_details):
                    print("Set Already Exists.")
                    continue

                exam_details.append(set_questions)

                # Ask if user wants to add more subjects
                choice = input(
                    "Do you want to add more set? (y/n): ").strip().lower()

            write_details(EXAM_FILE, exam_details)
            print("Set added successfully.")
            hold()
            clear()
            return
    print("Subject and topic not found.")
    hold()
    clear()


def greetpersonnel():
    display()
    print("|              Welcome Exam Unit Personnel            |")
    display()


def personnel_menu():
    """Main menu for academic administration."""
    if validate_login(PERSONNEL_FILE):
        while True:
            greetpersonnel()
            print(
                "\n1. Change Username and Password\n2. Create Sets\n3. Add questions\n4. Modify exam papers\n5. View Papers\n6. Logout\n")
            personnel_choice = input("Enter choice: ")
            clear()
            if personnel_choice == '1':
                update_credentials(PERSONNEL_FILE)
            elif personnel_choice == '2':
                view_subject_topics(SUBJECTS_FILE)
                create_sets(SUBJECTS_FILE)
            elif personnel_choice == '3':
                display_subject_topic_sets()
                add_questions(SUBJECTS_FILE)
            elif personnel_choice == '4':
                display_subject_topic_sets()
                modify_papers()
            elif personnel_choice == '5':
                display_subject_topic_sets()
                display_examsets()
                hold()
                clear()
            elif personnel_choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")
                hold()
                clear()
    else:
        print("Exiting due to failed login attempts.")


if __name__ == "__main__":
    personnel_menu()
