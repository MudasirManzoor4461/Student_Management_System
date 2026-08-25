import json
from exceptions.custom_exceptions import RepositoryError

def load_students():
    try:
        with open("data/students.json", "r") as f:
            student_list = json.load(f)
        return student_list
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    except OSError as error:
        raise RepositoryError(f"Error loading students: {error}")


def save_students(students):
    try:
        with open("data/students.json", 'w') as f:
            json.dump(students, f, indent=4)
    except OSError as error:
        raise RepositoryError(f"Error Saving students{error}")
