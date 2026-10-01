# Animal Shelter Management System

A command-line animal shelter management system built with Python.

This project was developed as a practical Python project to apply Object-Oriented Programming, file persistence, error handling, unit testing, and Git/GitHub workflow.

## Features

* Add new animals
* Find animals by ID
* Update animal information
* Delete animals
* Adopt animals
* Filter animals by status
* Validate user input
* Save animal data to JSON
* Load saved data when the application starts
* Automatic animal ID management
* Error handling for invalid operations
* Automated unit testing

## Technologies

* Python 3.14
* Object-Oriented Programming (OOP)
* JSON
* pytest
* Git
* GitHub
* Black
* Pylint

## Project Structure

```text
animal-shelter-management-system/
│
├── animal.py
├── shelter.py
├── data_manager.py
├── main.py
├── pytest.ini
│
├── data/
│   └── animals.json
│
└── tests/
    ├── test_animal.py
    ├── test_shelter.py
    ├── test_data_manager.py
    └── test_main.py
```

## How It Works

The application is divided into several components.

### Animal

The `Animal` class represents an animal in the shelter.

It manages:

* Animal ID
* Name
* Species
* Age
* Adoption status

It also provides methods for adoption, status management, data conversion, and displaying information.

### Shelter

The `Shelter` class manages the collection of animals.

It provides functionality for:

* Adding animals
* Finding animals
* Deleting animals
* Managing animal IDs

### Data Manager

The `data_manager.py` module handles persistence.

Animal information is stored in:

```text
data/animals.json
```

The application loads existing data when it starts and saves changes back to the JSON file.

### Main Application

`main.py` provides the command-line interface and handles user interaction and input validation.

## Installation

Clone the repository:

```bash
git clone https://github.com/aydingaffary/animal-shelter-management-system.git
```

Move into the project directory:

```bash
cd animal-shelter-management-system
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

Install pytest:

```bash
python -m pip install pytest
```

## Running the Application

Run:

```bash
python main.py
```

The application provides a menu for managing animals.

## Running Tests

The project contains **40 automated tests**.

Run the complete test suite with:

```bash
pytest
```

Expected result:

```text
40 passed
```

## Code Quality

The project was formatted with Black and checked with Pylint.

The final project achieved:

```text
Black: Passed
Pylint: 10/10
pytest: 40 passed
```

## What I Learned

This project was built to practice several core Python development concepts:

* Classes and objects
* Object-Oriented Programming
* Type validation
* Exception handling
* File I/O
* JSON serialization
* Modular Python development
* Unit testing with pytest
* Input validation
* Code formatting
* Static code analysis
* Git version control
* GitHub workflow

## Future Improvements

Possible future improvements include:

* Database support with SQLite
* A graphical or web interface
* User authentication
* Advanced search and filtering
* REST API integration
* Deployment as a web application

## Author

**Aydin gaffary**

GitHub:

https://github.com/aydingaffary

---

