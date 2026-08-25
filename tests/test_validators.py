from utils.validators import (
    validate_student_id,
    validate_name,
    validate_age,
    validate_email,
    validate_department
)


# -------------------------------
# Student ID Tests
# -------------------------------

def test_validate_student_id_valid():
    assert validate_student_id("STU001") is True
    assert validate_student_id("123") is True
    assert validate_student_id("ABC-123") is True


def test_validate_student_id_invalid():
    assert validate_student_id("") is False
    assert validate_student_id("   ") is False
    assert validate_student_id(None) is False


# -------------------------------
# Name Tests
# -------------------------------

def test_validate_name_valid():
    assert validate_name("Ali") is True
    assert validate_name("Muhammad Ali") is True
    assert validate_name("Ahmed Khan") is True


def test_validate_name_invalid():
    assert validate_name("") is False
    assert validate_name("   ") is False
    assert validate_name(None) is False


# -------------------------------
# Age Tests
# -------------------------------

def test_validate_age_valid():
    assert validate_age("1") is True
    assert validate_age("20") is True
    assert validate_age("100") is True
    assert validate_age(25) is True


def test_validate_age_invalid():
    assert validate_age("") is False
    assert validate_age("   ") is False
    assert validate_age("abc") is False
    assert validate_age("20abc") is False
    assert validate_age("0") is False
    assert validate_age("-5") is False
    assert validate_age("101") is False


# -------------------------------
# Email Tests
# -------------------------------

def test_validate_email_valid():
    assert validate_email("ali@gmail.com") is True
    assert validate_email("ahmed@yahoo.com") is True
    assert validate_email("user123@example.org") is True


def test_validate_email_invalid():
    assert validate_email("") is False
    assert validate_email("   ") is False
    assert validate_email("aligmai.com") is False
    assert validate_email("ali@gmail") is False
    assert validate_email("@gmail.com") is False
    assert validate_email("ali@") is False
    assert validate_email("ali@gmail.c") is False
    assert validate_email("ali@gmail.com@abc.com") is False


# -------------------------------
# Department Tests
# -------------------------------

def test_validate_department_valid():
    assert validate_department("Computer Science") is True
    assert validate_department("Software Engineering") is True
    assert validate_department("IT") is True


def test_validate_department_invalid():
    assert validate_department("") is False
    assert validate_department("   ") is False
    assert validate_department(None) is False