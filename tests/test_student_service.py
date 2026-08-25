import pytest

from services import student_service
from exceptions.custom_exceptions import (
    StudentAlreadyExistsError,
    StudentNotFoundError
)


def test_create_student(monkeypatch):

    monkeypatch.setattr(
        student_service,
        "load_students",
        lambda: []
    )

    saved_students = []

    def fake_save_students(students):
        saved_students.extend(students)

    monkeypatch.setattr(
        student_service,
        "save_students",
        fake_save_students
    )

    student = student_service.create_student(
        "TEST001",
        "Ali",
        20,
        "ali@gmail.com",
        "Computer Science"
    )

    assert student.student_id == "TEST001"
    assert student.name == "Ali"
    assert student.age == 20
    assert student.email == "ali@gmail.com"
    assert student.department == "Computer Science"

    assert len(saved_students) == 1


def test_create_student_duplicate_id(monkeypatch):

    existing_student = {
        "student_id": "TEST001",
        "name": "Ali",
        "age": 20,
        "email": "ali@gmail.com",
        "department": "Computer Science"
    }

    monkeypatch.setattr(
        student_service,
        "load_students",
        lambda: [existing_student]
    )

    with pytest.raises(StudentAlreadyExistsError):
        student_service.create_student(
            "TEST001",
            "Ahmed",
            22,
            "ahmed@gmail.com",
            "Software Engineering"
        )


def test_get_all_students(monkeypatch):

    students = [
        {
            "student_id": "TEST001",
            "name": "Ali",
            "age": 20,
            "email": "ali@gmail.com",
            "department": "Computer Science"
        },
        {
            "student_id": "TEST002",
            "name": "Ahmed",
            "age": 22,
            "email": "ahmed@gmail.com",
            "department": "Software Engineering"
        }
    ]

    monkeypatch.setattr(
        student_service,
        "load_students",
        lambda: students
    )

    result = student_service.get_all_students()

    assert result == students
    assert len(result) == 2


def test_search_student_found(monkeypatch):

    students = [
        {
            "student_id": "TEST001",
            "name": "Ali",
            "age": 20,
            "email": "ali@gmail.com",
            "department": "Computer Science"
        }
    ]

    monkeypatch.setattr(
        student_service,
        "load_students",
        lambda: students
    )

    result = student_service.search_student("TEST001")

    assert result is not None
    assert result["student_id"] == "TEST001"
    assert result["name"] == "Ali"


def test_search_student_not_found(monkeypatch):

    monkeypatch.setattr(
        student_service,
        "load_students",
        lambda: []
    )

    result = student_service.search_student("999")

    assert result is None


def test_remove_student(monkeypatch):

    students = [
        {
            "student_id": "TEST001",
            "name": "Ali",
            "age": 20,
            "email": "ali@gmail.com",
            "department": "Computer Science"
        },
        {
            "student_id": "TEST002",
            "name": "Ahmed",
            "age": 22,
            "email": "ahmed@gmail.com",
            "department": "Software Engineering"
        }
    ]

    monkeypatch.setattr(
        student_service,
        "load_students",
        lambda: students
    )

    saved_students = []

    def fake_save_students(data):
        saved_students.extend(data)

    monkeypatch.setattr(
        student_service,
        "save_students",
        fake_save_students
    )

    result = student_service.remove_student("TEST001")

    assert result is True
    assert len(saved_students) == 1
    assert saved_students[0]["student_id"] == "TEST002"


def test_remove_student_not_found(monkeypatch):

    monkeypatch.setattr(
        student_service,
        "load_students",
        lambda: []
    )

    with pytest.raises(StudentNotFoundError):
        student_service.remove_student("999")


def test_update_student(monkeypatch):

    students = [
        {
            "student_id": "TEST001",
            "name": "Ali",
            "age": 20,
            "email": "ali@gmail.com",
            "department": "Computer Science"
        }
    ]

    monkeypatch.setattr(
        student_service,
        "load_students",
        lambda: students
    )

    saved_students = []

    def fake_save_students(data):
        saved_students.extend(data)

    monkeypatch.setattr(
        student_service,
        "save_students",
        fake_save_students
    )

    result = student_service.update_student(
        "TEST001",
        "Ahmed",
        25,
        "ahmed@gmail.com",
        "Software Engineering"
    )

    assert result is True

    assert saved_students[0]["student_id"] == "TEST001"
    assert saved_students[0]["name"] == "Ahmed"
    assert saved_students[0]["age"] == 25
    assert saved_students[0]["email"] == "ahmed@gmail.com"
    assert saved_students[0]["department"] == "Software Engineering"


def test_update_student_not_found(monkeypatch):

    monkeypatch.setattr(
        student_service,
        "load_students",
        lambda: []
    )

    with pytest.raises(StudentNotFoundError):
        student_service.update_student(
            "999",
            "Ahmed",
            25,
            "ahmed@gmail.com",
            "Software Engineering"
        )