import json

import pytest

from repositories import student_repository
from exceptions.custom_exceptions import RepositoryError


def test_load_students_success(monkeypatch):
    students = [
        {
            "student_id": "TEST001",
            "name": "Ali",
            "age": 20,
            "email": "ali@gmail.com",
            "department": "Computer Science"
        }
    ]

    class FakeFile:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        def read(self):
            return json.dumps(students)

    monkeypatch.setattr(
        "builtins.open",
        lambda *args, **kwargs: FakeFile()
    )

    result = student_repository.load_students()

    assert result == students
    assert len(result) == 1


def test_load_students_file_not_found(monkeypatch):

    def fake_open(*args, **kwargs):
        raise FileNotFoundError

    monkeypatch.setattr(
        "builtins.open",
        fake_open
    )

    result = student_repository.load_students()

    assert result == []


def test_load_students_invalid_json(monkeypatch):

    class FakeFile:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        def read(self):
            return "INVALID JSON"

    monkeypatch.setattr(
        "builtins.open",
        lambda *args, **kwargs: FakeFile()
    )

    result = student_repository.load_students()

    assert result == []


def test_load_students_os_error(monkeypatch):

    def fake_open(*args, **kwargs):
        raise OSError("Disk error")

    monkeypatch.setattr(
        "builtins.open",
        fake_open
    )

    with pytest.raises(RepositoryError):
        student_repository.load_students()


def test_save_students_success(monkeypatch):

    students = [
        {
            "student_id": "TEST001",
            "name": "Ali",
            "age": 20,
            "email": "ali@gmail.com",
            "department": "Computer Science"
        }
    ]

    saved_data = {}

    class FakeFile:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

    def fake_open(*args, **kwargs):
        return FakeFile()

    def fake_dump(data, file, indent):
        saved_data["students"] = data
        saved_data["indent"] = indent

    monkeypatch.setattr(
        "builtins.open",
        fake_open
    )

    monkeypatch.setattr(
        student_repository.json,
        "dump",
        fake_dump
    )

    student_repository.save_students(students)

    assert saved_data["students"] == students
    assert saved_data["indent"] == 4


def test_save_students_os_error(monkeypatch):

    def fake_open(*args, **kwargs):
        raise OSError("Disk error")

    monkeypatch.setattr(
        "builtins.open",
        fake_open
    )

    with pytest.raises(RepositoryError):
        student_repository.save_students([])