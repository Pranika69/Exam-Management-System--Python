'''Student ID: NP069783'''
'''
Steps to run the main.py
1. Go to the the folder, then run the folder from the cmd.
2. In cmd, type cmd ., it will open the folder in VS code, then run it.
'''

import sys
import os
path=os.getcwd().replace("\\","\\\\")
sys.path.insert(0, f"{path}")
from Admin_Functions.admin import admin_menu
from Main_Functions.additionalfunctions import *
from Lecturer_Functions.lecturer import lecturer_menu
from Personnel_Functions.Personnel import personnel_menu


def main():
    flag = True
    while flag:
        clear()
        display()
        print("|     Welcome to Test Questions Management System     |")
        display()
        print("\nSelect your designation.")
        designation_choice = input(
            "\n1. Admin\n2. Lecturer\n3. Exam Unit Personnel\n4. Exit\n\n")
        
        if designation_choice == '1':
            admin_menu()

        elif designation_choice == '2':
            lecturer_menu()

        elif designation_choice == '3':
            personnel_menu()

        elif designation_choice == '4':
            print("\nExiting............")
            flag = False

        else:
            print("\nInvalid Input! Try again.\n")
            hold()
            clear()
            continue

if __name__ == "__main__":
    main()
