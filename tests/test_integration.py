import json

from services import student_service
from repositories import student_repository


def test_student_full_flow(tmp_path, monkeypatch):

    # Temporary JSON file
    test_file = tmp_path / "students.json"

    test_file.write_text("[]")

    # Repository ko temporary file use karwa rahe hain
    def fake_load_students():
        with open(test_file, "r") as file:
            return json.load(file)

    def fake_save_students(students):
        with open(test_file, "w") as file:
            json.dump(students, file, indent=4)

    monkeypatch.setattr(
        student_service,
        "load_students",
        fake_load_students
    )

    monkeypatch.setattr(
        student_service,
        "save_students",
        fake_save_students
    )

    # -----------------------------
    # 1. CREATE
    # -----------------------------

    student = student_service.create_student(
        "INT001",
        "Ali",
        20,
        "ali@gmail.com",
        "Computer Science"
    )

    assert student.student_id == "INT001"

    # -----------------------------
    # 2. LOAD
    # -----------------------------

    students = student_service.get_all_students()

    assert len(students) == 1
    assert students[0]["student_id"] == "INT001"

    # -----------------------------
    # 3. SEARCH
    # -----------------------------

    found_student = student_service.search_student("INT001")

    assert found_student is not None
    assert found_student["name"] == "Ali"

    # -----------------------------
    # 4. UPDATE
    # -----------------------------

    result = student_service.update_student(
        "INT001",
        "Ahmed",
        25,
        "ahmed@gmail.com",
        "Software Engineering"
    )

    assert result is True

    updated_student = student_service.search_student("INT001")

    assert updated_student["name"] == "Ahmed"
    assert updated_student["age"] == 25
    assert updated_student["email"] == "ahmed@gmail.com"
    assert updated_student["department"] == "Software Engineering"

    # -----------------------------
    # 5. DELETE
    # -----------------------------

    result = student_service.remove_student("INT001")

    assert result is True

    # -----------------------------
    # 6. VERIFY DELETE
    # -----------------------------

    students = student_service.get_all_students()

    assert students == []