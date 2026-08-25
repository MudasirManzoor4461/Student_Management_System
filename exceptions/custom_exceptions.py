
class StudentNotFoundError(Exception):
    def __init__(self, student_id):
        self.student_id = student_id
        message = f"Student with ID {student_id} not found."
        super().__init__(message)


class StudentAlreadyExistsError(Exception):
    def __init__(self, student_id):
        self.student_id = student_id
        message = f"Student with ID {student_id} already exists."
        super().__init__(message)


class RepositoryError(Exception):
    def __init__(self, message):
        super().__init__(message)