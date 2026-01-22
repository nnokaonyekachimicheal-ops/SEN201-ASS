"""
Project Title: Student Management System
Course: SEN 201
Name: NNOKA ONYEKACHI MICHEAL
Matric No: 24/14841
Department: Computer Science
"""

students = []

def add_student():
    name = input("Enter student name: ")
    matric_no = input("Enter matric number: ")
    department = input("Enter department: ")
    
    student = {
        "name": name,
        "matric_no": matric_no,
        "department": department
    }
    
    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students available.\n")
        return
    
    for index, student in enumerate(students, start=1):
        print(f"{index}. Name: {student['name']}, "
              f"Matric No: {student['matric_no']}, "
              f"Department: {student['department']}")
    print()

def main():
    while True:
        print("==== Student Management System ====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
