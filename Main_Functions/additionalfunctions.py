'''Student ID: NP069599'''

import os
import re
from datetime import datetime,date
 
def display():
  print("|*****************************************************|")

def clear():
  os.system('cls')

def hold():
  os.system("PAUSE")

def generate_id(lecturers):
    """Generate a unique ID based on existing entries."""
    if not lecturers:
        return '1'  # Assuming starting ID is '1'
    else:
        # Generate ID based on the last ID in the list
        last_id = int(lecturers[-1]['ID'])
        new_id = str(last_id + 1)
        return new_id


def calculate_age(dob):
    """Calculate age based on date of birth."""
    today = date.today()
    birth_date = datetime.strptime(dob, '%Y-%m-%d').date()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


def get_strong_password():
    """Ensure password meets strong criteria (8 characters with numbers, uppercase, lowercase, and special characters)."""
    while True:
        password = input("Enter lecturer password (at least 8 characters with numbers, uppercase, lowercase, and special characters): ")

        # Check for minimum length
        if len(password) < 8:
            print("Password must be at least 8 characters.")
            continue

        has_digit = any(char.isdigit() for char in password)
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        has_special = any(not char.isalnum() for char in password)

        # Check for each criteria
        if not has_digit:
            print("Password must contain at least one digit (0-9).")
        elif not has_upper:
            print("Password must contain at least one uppercase letter (A-Z).")
        elif not has_lower:
            print("Password must contain at least one lowercase letter (a-z).")
        elif not has_special:
            print("Password must contain at least one special character.")
        else:
            # If all criteria are met, return the password
            return password
        

def get_non_empty_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input.lower()
        print("Input cannot be empty. Please enter again.")

def get_phone_number():
    """Validate and return a 10-digit phone number."""
    while True:
        phone_number = input("Enter contact number (10 digits): ").strip()
        if re.match(r'^\d{10}$', phone_number):
            return phone_number
        print("Invalid phone number format. Please enter 10 digits.")


def get_date_of_birth():
    """Validate and return a date of birth in format dd-mm-yyyy."""
    while True:
        dob = input("Enter date of birth (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(dob, '%Y-%m-%d')
            return dob
        except ValueError:
            print("Incorrect date format. Please enter date in YYYY-MM-DD format.")


def get_citizenship():
    """Validate and return citizenship in format xx-xx-xx-xxxxx."""
    while True:
        citizenship = input("Enter citizenship (xx-xx-xx-xxxxx): ").strip()
        if re.match(r'^\w{2}-\w{2}-\w{2}-\w{5}$', citizenship):
            return citizenship
        print("Invalid citizenship format. Please enter in xx-xx-xx-xxxxx format.")


def get_email():
    """Validate and return an email address ending with @gmail.com."""
    while True:
        email = input("Enter email address: ").strip().lower()
        if email.endswith('@gmail.com'):
            return email
        print("Invalid email address. Please enter an address ending with @gmail.com.")



