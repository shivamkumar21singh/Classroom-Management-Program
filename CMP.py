import json

def login_as_admin():
    teacher_id = input("Enter Teacher ID: ")
    password = input("Enter Password: ")

    # Check if the credentials are valid
    if validate_admin_credentials(teacher_id, password):
        admin_menu()
    else:
        print("Invalid credentials. Please try again.")
        login_as_admin()

def validate_admin_credentials(teacher_id, password):
    # Load teacher data from file
    with open("teacher_data.json", "r") as file:
        teachers = json.load(file)

    # Check if credentials are valid
    return teachers.get(teacher_id, {}).get("password") == password

def admin_menu():
    while True:
        print("\nADMIN MENU:")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Edit Student Details")
        print("4. Add CGPA")
        print("5. Take Attendance")
        print("6. Logout")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            edit_student_details()
        elif choice == "4":
            add_cgpa()
        elif choice == "5":
            take_attendance()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    section = input("Enter Section: ")
    fees = input("Paid Fees (Y/N): ")
    password = input("Enter Password: ")

    # Load existing student data
    students = load_students()

    # Add new student
    students[roll] = {"name": name, "section": section, "fees": fees, "password": password}

    # Save updated data to file
    save_students(students)

    print(f"Student {name} added successfully.")

def remove_student():
    roll = input("Enter Roll Number to remove: ")

    # Load existing student data
    students = load_students()

    # Check if student exists
    if roll in students:
        del students[roll]
        save_students(students)
        print(f"Student with Roll Number {roll} removed successfully.")
    else:
        print(f"Student with Roll Number {roll} not found.")

def edit_student_details():
    roll = input("Enter Roll Number to edit details: ")

    # Load existing student data
    students = load_students()

    # Check if student exists
    if roll in students:
        print("\nCURRENT STUDENT DETAILS:")
        print(f"1. Name: {students[roll]['name']}")
        print(f"2. Section: {students[roll]['section']}")
        print(f"3. Paid Fees: {students[roll]['fees']}")
        print("4. Cancel")

        choice = input("Enter the number corresponding to the detail you want to edit (1-4): ")

        if choice == "1":
            students[roll]['name'] = input("Enter new Name: ")
        elif choice == "2":
            students[roll]['section'] = input("Enter new Section: ")
        elif choice == "3":
            students[roll]['fees'] = input("Update Paid Fees (Y/N): ")
        elif choice == "4":
            pass  # Cancel editing
        else:
            print("Invalid choice. Editing canceled.")

        # Save updated data to file
        save_students(students)

        print(f"Student details for Roll Number {roll} updated successfully.")
    else:
        print(f"Student with Roll Number {roll} not found.")

def add_cgpa():
    roll = input("Enter Roll Number: ")
    cgpa = input("Enter CGPA: ")

    # Load existing student data
    students = load_students()

    # Check if student exists
    if roll in students:
        students[roll]["cgpa"] = cgpa
        save_students(students)
        print(f"CGPA added for student with Roll Number {roll}.")
    else:
        print(f"Student with Roll Number {roll} not found.")

def take_attendance():
    # Load existing student data
    students = load_students()

    # Take attendance for all students
    for roll, student in students.items():
        attendance = input(f"Is {student['name']} present? (Y/N): ")
        student["attendance"] = attendance

    # Save updated data to file
    save_students(students)

    print("Attendance taken successfully.")

def load_students():
    try:
        with open("students_data.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = {}
    return students

def save_students(students):
    with open("students_data.json", "w") as file:
        json.dump(students, file, indent=2)

def main():
    print("Welcome to Classroom Management Program")

    while True:
        print("\nLOGIN MENU:")
        print("1. Login as ADMIN")
        print("2. Login as STUDENT")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            login_as_admin()
        elif choice == "2":
            login_as_student()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def login_as_student():
    roll = input("Enter Roll Number: ")
    password = input("Enter Password: ")

    # Load existing student data
    students = load_students()

    # Check if student exists and credentials are valid
    if roll in students and students[roll].get("password") == password:
        student_menu(roll, students)
    else:
        print("Invalid credentials or student not found. Please try again.")

def student_menu(roll, students):
    # Display student information
    print("\nSTUDENT INFO:")
    print(f"Roll Number: {roll}")
    print(f"Name: {students[roll]['name']}")
    print(f"Section: {students[roll]['section']}")

    while True:
        print("\nSTUDENT MENU:")
        print("1. Check CGPA")
        print("2. Check Attendance")
        print("3. Logout")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            check_cgpa(roll, students)
        elif choice == "2":
            check_attendance(roll, students)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def check_cgpa(roll, students):
    # Check if CGPA exists for the student
    cgpa = students[roll].get("cgpa", "CGPA not available")
    print(f"CGPA for Roll Number {roll}: {cgpa}")

def check_attendance(roll, students):
    # Check if attendance exists for the student
    attendance = students[roll].get("attendance", "Attendance not available")
    print(f"Attendance for Roll Number {roll}: {attendance}")

if __name__ == "__main__":
    main()