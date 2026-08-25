# 🎓 Student Management System

A **modular, console-based Student Management System built with Python**.

This project demonstrates how to build a real-world Python application using **layered architecture, CRUD operations, JSON-based data persistence, custom exceptions, input validation, logging, and automated testing with pytest**.

The project is designed to practice clean code organization and software engineering principles rather than keeping everything inside a single Python file.

---

## 📌 Project Overview

The Student Management System allows users to manage student records through an interactive command-line interface.

Users can:

* ➕ Add new students
* 📋 View all students
* 🔍 Search for a student
* 🗑️ Delete a student
* ✏️ Update student information
* 🚪 Exit the application

Student records are stored persistently in a JSON file, so the data remains available after the application is closed.

The application also includes validation, custom exception handling, logging, and automated tests.

---

## ✨ Features

### 👨‍🎓 Student Management

* Create student records
* View all registered students
* Search students by Student ID
* Update student information
* Delete student records
* Prevent duplicate Student IDs

### ✅ Input Validation

The application validates:

* Student ID
* Student name
* Age
* Email
* Department

Invalid input is rejected and the user is asked to enter the information again.

### 🛡️ Exception Handling

Custom exceptions are used to handle application-specific errors such as:

* Student not found
* Duplicate student
* Repository/file errors

This keeps error handling organized and easier to maintain.

### 💾 Data Persistence

Student records are stored in:

```text
data/students.json
```

The repository layer handles reading and writing student data.

### 📝 Logging

The application uses Python's `logging` module to record important events such as:

* Application startup
* Student creation
* Student deletion
* Student updates
* Student searches
* Failed operations
* Repository-related events

Logs are stored in:

```text
logs/student_management.log
```

### 🧪 Automated Testing

The project uses **pytest** for automated testing.

The test suite covers:

* Student service
* Student repository
* Validators
* Integration behavior
* Success cases
* Failure cases
* Exception cases

Current test suite:

```text
26 tests passed
```

---

## 🏗️ Project Architecture

The application follows a layered structure:

```text
User
 │
 ▼
main.py
 │
 ▼
Services Layer
 │
 ▼
Repository Layer
 │
 ▼
JSON Data Storage
```

Supporting components:

```text
Validators ───────► Input Validation
Exceptions ───────► Error Handling
Logger ───────────► Application Logging
Tests ────────────► Automated Verification
```

This separation makes the application easier to understand, test, maintain, and extend.

---

## 📂 Project Structure

```text
Pyhton_Project/
│
├── data/
│   └── students.json
│
├── exceptions/
│   └── custom_exceptions.py
│
├── logs/
│   └── student_management.log
│
├── models/
│   └── student.py
│
├── repositories/
│   └── student_repository.py
│
├── services/
│   ├── __init__.py
│   └── student_service.py
│
├── tests/
│   ├── test_student_service.py
│   ├── test_student_repository.py
│   ├── test_validators.py
│   └── test_integration.py
│
├── utils/
│   ├── logger.py
│   └── validators.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔧 Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Core programming language |
| JSON         | Data persistence          |
| Pytest       | Automated testing         |
| Logging      | Application logging       |
| Git / GitHub | Version control           |
| VS Code      | Development environment   |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MudasirManzoor4461/Student_Management_System
```

Move into the project directory:

```bash
cd Pyhton_Project
```

### 2. Create a Virtual Environment

```bash
python -m venv myenv
```

### 3. Activate the Virtual Environment

#### Windows PowerShell

```powershell
myenv\Scripts\Activate.ps1
```

#### Windows CMD

```cmd
myenv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
py main.py
```

or:

```bash
python main.py
```

---

## 🖥️ Application Usage

After starting the application, the main menu is displayed:

### Main Menu

![Main Menu](screenshots/main_menu.png)

The user can select an operation from options **1–6**.

---

## 📸 Screenshots

### ➕ Add Student

The application validates the student's information before creating the record.

![Add Student](screenshots/add_student.png)

### 📋 View All Students

Displays all students currently stored in the system.

![View Students](screenshots/view_students.png)

### 🔍 Search Student

Allows the user to search for a student using the Student ID.

![Search Student](screenshots/search_student.png)

### ✏️ Update Student

Allows existing student information to be modified.

![Update Student](screenshots/update_student.png)

### 🗑️ Delete Student

Removes an existing student record from the system.

![Delete Student](screenshots/delete_student.png)

---

## 🧪 Running Tests

Run the complete test suite with:

```bash
py -m pytest -v
```

Example result:

```text
26 passed
```

![Pytest Results](screenshots/pytest.png)

A successful test run confirms that the implemented functionality is behaving as expected across the tested components.

---

## 🧩 Testing Strategy

The project uses multiple levels of testing.

### Unit Tests

Individual functions and components are tested independently.

Examples:

* Validators
* Student service functions
* Repository functions

### Integration Tests

Integration tests verify that different layers of the application work correctly together.

For example:

```text
Service
   ↓
Repository
   ↓
JSON Storage
```

### Edge Cases

The tests also cover situations such as:

* Searching for a non-existing student
* Deleting a non-existing student
* Updating a non-existing student
* Creating a duplicate Student ID
* Invalid user input
* Empty data

---

## 🛡️ Error Handling

The project uses custom exceptions instead of relying only on generic exceptions.

Examples include:

```text
StudentNotFoundError
StudentAlreadyExistsError
RepositoryError
```

This provides clearer error messages and keeps application logic organized.

---

## 📝 Logging

Important application events are recorded in:

```text
logs/student_management.log
```

Example events include:

```text
INFO    - Student Management System started
INFO    - Student Created Successfully
INFO    - Student Updated successfully
INFO    - Student deleted successfully
WARNING - Student not found
WARNING - Update Failed
```

Logging makes it easier to monitor application behavior and troubleshoot problems.

---

## 💡 What This Project Demonstrates

This project demonstrates practical Python development concepts including:

* Functions
* Classes and Objects
* Object-Oriented Programming
* Modular programming
* Package organization
* CRUD operations
* JSON file handling
* Exception handling
* Custom exceptions
* Input validation
* Logging
* Unit testing
* Integration testing
* pytest
* Virtual environments
* Separation of responsibilities
* Basic software architecture

---

## 🔮 Future Improvements

Possible future improvements include:

* [ ] Add a graphical user interface
* [ ] Replace JSON storage with SQLite/MySQL
* [ ] Add student sorting and filtering
* [ ] Add pagination for large student lists
* [ ] Add authentication and user roles
* [ ] Add automated CI/CD testing with GitHub Actions
* [ ] Add API support using FastAPI or Flask
* [ ] Add database-backed search
* [ ] Improve the CLI user experience

---

## 📈 Learning Goals

The main goal of this project is to move from writing small Python programs to building a **structured, maintainable, and testable application**.

It provides practical experience with how different components of a Python application communicate with each other:

```text
                ┌──────────────┐
                │    main.py   │
                └──────┬───────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Student Service │
              └────────┬────────┘
                       │
                       ▼
             ┌───────────────────┐
             │ Student Repository│
             └─────────┬─────────┘
                       │
                       ▼
                ┌────────────┐
                │ students.json │
                └────────────┘
```

---

## 👨‍💻 Author

**Mudasir Manzoor**

Computer Science Student | Python Developer | Software Engineering Learner

---

## ⭐ Project Status

**Status:** Completed ✅

**Test Status:** 26 Tests Passed ✅

**Data Storage:** JSON

**Testing Framework:** pytest

**Language:** Python
