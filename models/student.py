class Student:
    def __init__(self, student_id, name, age, email, department):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.department = department

    def get_info(self):
        return f"Student_ID: {self.student_id} | Name:{self.name} | Age:{self.age} | Email: {self.email}| Department: {self.department}"

    def __str__(self):
        return self.get_info()

    def to_dict(self):
        return {"student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "department": self.department
        }