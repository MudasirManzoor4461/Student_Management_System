from services.student_service import (create_student, get_all_students, search_student, 
        remove_student, update_student)
from utils.validators import(validate_student_id, validate_name, validate_age, validate_email,validate_department)
from exceptions.custom_exceptions import StudentNotFoundError, StudentAlreadyExistsError, RepositoryError
from utils.logger import logger

def add_student():
    print("\n------ Enter Student Details ------")
    while True:
        student_id = input("Student ID: ")

        if not validate_student_id(student_id):
            print("Invalid Student ID.")
            continue

        student_id = student_id.strip()

        if search_student(student_id):
            print("Student ID already exists.")
            continue

        break
    while True:
        name = input("Student Name: ")
        if validate_name(name):
            name = name.strip()
            break

        print("Please Enter name.")

    while True:
        age = input("Student Age: ")

        if validate_age(age):
             age = int(age.strip())
             break
        
        print("Invalid Age")

    while True:
        email = input("Student Email: ")
        if validate_email(email):
            email = email.strip()
            break

        print("Invalid Email.")

    while True:
        department = input("Student Department: ")
        if validate_department(department):
            department = department.strip()
            break
        
        print("Invalid Department")

    try:
        create_student(student_id, name, age, email, department)
        print("Student Addded Successfully")
    except StudentAlreadyExistsError as error:
        print(error)
    except RepositoryError as error:
        print(error)

def view_students():
    print("\n---- All Students List ------")
    try:
        students = get_all_students()
        if not students:
            print("No students record found")
        else:
            for std in students:
                print(
                f"ID: {std['student_id']} | Name: {std['name']} | Dept: {std['department']}"
                )
    except RepositoryError as error:
        print(error)


def search_student_menu():
    print("\nSearch Student is here!")
    search_id = input("Enter Student Id: ").strip()
    try:
        student = search_student(search_id)
        if not student:
            print("No student found for this Id")
        else:
                print("\nStudent Found")
                print(
                f"ID: {student['student_id']} | Name: {student['name']} | Dept: {student['department']}"            )

    except RepositoryError as error:
        print(error)

def delete_student_menu():
    print("\n---- Delete Student ----")
    std_id = input("Student Id: ").strip()

    try:
        remove_student(std_id)
        print("Delete Student Successfully")
    except StudentNotFoundError as error:
        print(error)
    except RepositoryError as error:
        print(error)


def update_student_menu():
    print("\n------ Update Student -------")

    while True:
        std_id = input("Enter student id to update: ")
        if validate_student_id(std_id):
            std_id = std_id.strip()
            break
        print("Invalid Student ID format!")
    try:
        student = search_student(std_id)
        if not student:
            print("Student Id not found!")
            return

        print(f"\nStudent Found: {student['name']}")
        print("Enter New Details:")

        while True:
            new_name = input("New Name: ")
            if validate_name(new_name):
                new_name = new_name.strip()
                break
            print("Invalid Name!")

        while True:
            new_age = input("New Age (1-100): ")
            if validate_age(new_age):
                new_age = int(new_age.strip())
                break
            print("Invalid Age!")

        while True:
            new_email = input("New Email: ")
            if validate_email(new_email):
                new_email = new_email.strip()
                break
            print("Invalid Email format!")

        while True:
            new_department = input("New Department: ")
            if validate_department(new_department):
                new_department = new_department.strip()
                break
            print("Invalid Department!")

        success = update_student(
            std_id, new_name, new_age, new_email, new_department
        )

        if success:
            print("\nStudent Details Updated Successfully!")
    except StudentNotFoundError as error:
        print(error)
    except RepositoryError as error:
        print(error)


def main():
    logger.info("Student Management System started")

    while True:
        print("\n******Student Management System******")
        print("1. Add Students")
        print("2. View all Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")

        choice = input("\nEnter Choice (1 to 6): ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student_menu()
        elif choice == "4":
            delete_student_menu()
        elif choice == "5":
            update_student_menu()
        elif choice == "6":
            print("\nGood Bye Program Closed")
            break
        else:
            print("Invalid Input! please select 1, 2 3 4 5 or 6.")

if __name__ =="__main__":
    main()


