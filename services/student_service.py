from models.student import Student
from repositories.student_repository import load_students, save_students
from exceptions.custom_exceptions import StudentNotFoundError, StudentAlreadyExistsError
from utils.logger import logger


def create_student(student_id, name, age, email, department):

    if search_student(student_id):
        raise StudentAlreadyExistsError(student_id)
    
    students_list = load_students()
    student_obj = Student(student_id, name, age, email, department)

    student_dict = student_obj.to_dict()
    students_list.append(student_dict)

    save_students(students_list)
    logger.info(f"Student Created Successfully: {student_id}")
    return student_obj


def get_all_students():
    student_list = load_students()
    logger.info(f"Total Students loaded: {len(student_list)}")
    return student_list


def search_student(student_id):
    students = load_students()
    for student in students:
        if student["student_id"] == student_id:
            return student
    logger.warning(f"Student not found: {student_id}")
    return None


def remove_student(student_id):
    students = load_students()
    for student in students:
        if student["student_id"] == student_id:
            students.remove(student)
            save_students(students)
            logger.info(f"Student deleted successfully: {student_id}")
            return True
        
    logger.warning(f"Delete failed, student not found {student_id}")
        
    raise StudentNotFoundError(student_id)
    

def update_student(student_id, new_name, new_age, new_email, new_department):
    students = load_students()
    for student in students:
        if student["student_id"] == student_id:
            student["name"] = new_name
            student["department"] = new_department
            student["age"] = new_age
            student["email"] = new_email
            save_students(students)
            logger.info(f"Student Updated successfully: {student_id}")
            return True
    logger.warning(f"Update Failed, Student not found: {student_id}")
    raise StudentNotFoundError(student_id)