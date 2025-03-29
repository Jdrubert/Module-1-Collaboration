# Author: [Jaden Drubert]
# File name: student_gpa_app.py
# Description: This app accepts student names and GPAs, then checks if the student qualifies for the Dean's List or Honor Roll based on their GPA.

def main():
    while True:
        last_name = input("Enter the studet's last name (or 'ZZZ' to quit): ")
        if last_name == 'ZZZ':
            break

        first_name = input("Enter the student's first name: ")

        # Ask for the student's GPA as a float
        while True:
            gpa_input = input("Enter the student's GPA: ")

            # Check if the GPA is a valid float
            if gpa_input.replace('.', '', 1).isdigit() and gpa_input.count('.') < 2:
                gpa = float(gpa_input)
                break
            else:
                print("Invalid GPA input. Please enter a valid number.")

        # Check if the student made the Dean's List
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List!")
        
        # Check if the student made the Honor Roll
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll!")
        elif gpa < 3.25:
            print(f"{first_name} {last_name} has not made Honor Roll or the Dean's List.")
main()