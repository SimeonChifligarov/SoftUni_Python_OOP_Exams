# SoftUni Python OOP Exams

### Object-Oriented Programming, Exam Preparation, Practical OOP Design & Unit Testing

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![OOP](https://img.shields.io/badge/Focus-Object--Oriented%20Programming-orange)](#topics-covered)
[![Testing](https://img.shields.io/badge/Testing-unittest-green)](https://docs.python.org/3/library/unittest.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A collection of solved **Python Object-Oriented Programming exam preparation exercises, a SoftUni OOP practical exam project, and unit-testing exercises** created while studying Python OOP at [SoftUni](https://softuni.bg/).

The repository focuses on applying core object-oriented programming principles in larger, structured problems rather than isolated syntax exercises.

---

> [!IMPORTANT]
> This is an **independent educational repository** containing my personal solutions and implementations created during the learning process.
>
> Original exam descriptions, project skeletons, judge requirements, and other materials provided by **SoftUni** remain the property of their respective authors and rights holders. This repository is not an official SoftUni repository.

## Table of Contents

- [Overview](#overview)
- [Topics Covered](#topics-covered)
- [Learning Objectives](#learning-objectives)
- [Repository Structure](#repository-structure)
- [Real Exam Project — Bakery](#real-exam-project--bakery)
- [Unit Testing — PetShop](#unit-testing--petshop)
- [Exam Preparation](#exam-preparation)
- [Getting Started](#getting-started)
- [Working with the Repository](#working-with-the-repository)
- [Educational Scope](#educational-scope)
- [Academic Integrity](#academic-integrity)
- [SoftUni Attribution and Disclaimer](#softuni-attribution-and-disclaimer)
- [License](#license)
- [Author](#author)

## Overview

This repository documents my preparation for and work on the **Python OOP examination at SoftUni**.

The exercises are centered around designing applications from collections of interacting classes while following predefined business rules, validation requirements, inheritance hierarchies, and public interfaces.

The repository includes:

- A complete OOP project from the **August 2021 Python OOP exam**
- Five solved exam-preparation sets
- Class hierarchies using inheritance and abstraction
- Encapsulated state through properties and validation
- Composition and interaction between domain objects
- Business-logic orchestration through service/controller classes
- Custom string representations
- Exception handling and input validation
- Unit testing with Python's built-in `unittest` framework
- Tests for valid behavior, invalid input, exceptions, and state changes

The main objective is not simply to make the code pass a judge, but to practice translating a specification into a structured object-oriented model.

## Topics Covered

### Object-Oriented Design

- Classes and objects
- Object initialization
- Instance attributes
- Class responsibilities
- Separation of concerns
- Object collaboration
- Domain modeling
- Composition
- Reusable class hierarchies

### Encapsulation

- Private attributes
- Properties
- Property setters
- Data validation
- Controlled object state
- Guarding class invariants
- Validation through exceptions

### Inheritance

- Base classes
- Specialized subclasses
- Shared behavior
- Method reuse
- Extending parent functionality
- Modeling `is-a` relationships

Examples from the real exam project include hierarchies such as:

```text
BakedFood
├── Bread
└── Cake

Drink
├── Tea
└── Water

Table
├── InsideTable
└── OutsideTable
```

### Abstraction

- Abstract base classes
- Python's `abc` module
- `ABC`
- `@abstractmethod`
- Defining common interfaces for related classes

### Polymorphism

- Working with subclass instances through common abstractions
- Shared interfaces with specialized behavior
- Collections containing related object types

### Validation and Exceptions

- Constructor validation
- Property validation
- `ValueError`
- Application-specific error conditions
- Preventing invalid object states

### Special Methods

- `__init__`
- `__repr__`
- Object representation
- Formatting domain objects for application output

### Unit Testing

- `unittest.TestCase`
- Test fixtures with `setUp()`
- Assertions
- Exception testing
- State verification
- Return-value verification
- Boundary and invalid-input cases

## Learning Objectives

By working through the exercises in this repository, the learner should be able to:

- Translate written requirements into Python class models
- Identify appropriate classes and their responsibilities
- Design inheritance hierarchies without unnecessarily duplicating behavior
- Use abstract base classes to define shared interfaces
- Protect internal state through encapsulation
- Validate object construction and modification
- Coordinate multiple domain objects through a central application class
- Implement business rules involving collections of objects
- Raise meaningful exceptions for invalid operations
- Write readable object representations
- Test classes independently with `unittest`
- Verify both returned results and changes in internal state
- Test expected exceptions and edge cases
- Structure a multi-file Python OOP project

## Repository Structure

```text
SoftUni_Python_OOP_Exams/
│
├── 00_Preparation/
│   ├── 02_Python_OOP_Exam_Prep/
│   │   ├── 01_Structure/
│   │   ├── 02_Functionality/
│   │   └── 03_Unit_Testing/
│   │
│   ├── OLD_VER_Exam_Prep_1/
│   ├── OLD_VER_Exam_Prep_2/
│   ├── OLD_VER_Exam_Prep_3/
│   ├── OLD_VER_Exam_Prep_4/
│   └── README.md
│
├── project_SoftUni_OOP_Python_Aug_2021/
│   ├── baked_food/
│   │   ├── baked_food.py
│   │   ├── bread.py
│   │   └── cake.py
│   │
│   ├── drink/
│   │   ├── drink.py
│   │   ├── tea.py
│   │   └── water.py
│   │
│   ├── table/
│   │   ├── table.py
│   │   ├── inside_table.py
│   │   └── outside_table.py
│   │
│   ├── __init__.py
│   └── bakery.py
│
├── testing_class_unittest/
│   └── test.py
│
├── .gitignore
├── LICENSE
└── README.md
```

| Directory | Purpose |
| --- | --- |
| [`00_Preparation`](00_Preparation) | Solved OOP exam-preparation exercises |
| [`00_Preparation/02_Python_OOP_Exam_Prep`](00_Preparation/02_Python_OOP_Exam_Prep) | Preparation organized into structure, functionality, and unit-testing stages |
| [`project_SoftUni_OOP_Python_Aug_2021`](project_SoftUni_OOP_Python_Aug_2021) | Solution to the August 2021 practical OOP project |
| [`testing_class_unittest`](testing_class_unittest) | Standalone `unittest` exercise for the `PetShop` class |

## Real Exam Project — Bakery

The main practical project in the repository is a **Bakery management domain model** from the August 2021 Python OOP exam.

The solution models several related object families and brings them together through the `Bakery` class.

### Baked Food Hierarchy

```text
BakedFood (abstract)
├── Bread
└── Cake
```

`BakedFood` defines common information and behavior for baked products, including concepts such as:

- Name
- Portion
- Price
- Validation
- Human-readable representation

Concrete food classes specialize this base abstraction.

### Drink Hierarchy

```text
Drink (abstract)
├── Tea
└── Water
```

The drink abstraction models shared attributes such as:

- Name
- Portion
- Price
- Brand

Validation protects the objects from invalid names, portions, brands, and other unsupported state.

### Table Hierarchy

```text
Table
├── InsideTable
└── OutsideTable
```

Tables represent the seating component of the bakery and are responsible for concepts including:

- Table number
- Capacity
- Reservation state
- Number of customers
- Food orders
- Drink orders
- Bill calculation
- Clearing a table after customers leave

### Bakery Service Class

The central `Bakery` class coordinates the individual domain objects.

Its responsibilities include:

- Maintaining the food menu
- Maintaining the drinks menu
- Managing available tables
- Adding food
- Adding drinks
- Adding tables
- Preventing duplicate menu items or table numbers
- Reserving suitable tables
- Processing food orders
- Processing drink orders
- Handling unavailable menu items
- Calculating a table's bill
- Clearing tables after customers leave
- Tracking total bakery income
- Reporting free tables

This structure demonstrates an important OOP principle: individual domain classes manage their own state and behavior, while a higher-level class coordinates interactions between them.

## Unit Testing — PetShop

The repository also contains a dedicated testing exercise based on a `PetShop` class.

The tests use Python's built-in:

```python
from unittest import TestCase, main
```

The test suite covers behavior such as:

### Initialization

Verifying that a newly created shop contains the expected:

- Name
- Empty food inventory
- Empty pet collection

### Adding Food

Tests cover:

- Rejecting zero or negative quantities
- Adding a previously unavailable food
- Increasing the quantity of existing food
- Correct return messages
- Correct updates to internal state

### Adding Pets

Tests verify:

- Successfully adding a new pet
- Preventing duplicate pet names
- Correct exception messages
- Preservation of object state after invalid operations

### Feeding Pets

Tests cover:

- Invalid pet names
- Missing food
- Insufficient food quantities
- Restocking behavior
- Successful feeding
- Correct reduction of food inventory

### Object Representation

The suite also verifies the formatted representation returned by `repr()`.

The exercise demonstrates that effective testing should verify more than return values. Tests should also inspect:

- Mutated state
- Collections
- Numeric quantities
- Raised exceptions
- Exception messages
- Boundary conditions

> [!NOTE]
> The testing exercise follows the package structure expected by the original SoftUni task and imports `PetShop` as `project.pet_shop.PetShop`. If the test is executed independently, the corresponding exercise implementation must be available using that package layout.

## Exam Preparation

The [`00_Preparation`](00_Preparation) directory contains **five solved preparation sets**:

```text
02_Python_OOP_Exam_Prep
OLD_VER_Exam_Prep_1
OLD_VER_Exam_Prep_2
OLD_VER_Exam_Prep_3
OLD_VER_Exam_Prep_4
```

The preparation material reinforces the complete workflow used in Python OOP exams:

1. Read the specification carefully.
2. Identify the required class hierarchy.
3. Implement the required project structure.
4. Add constructors and validation.
5. Implement inheritance and shared behavior.
6. Add application functionality.
7. Handle invalid operations.
8. Match the required output format.
9. Write or complete unit tests.
10. Verify behavior against the specification.

The newer preparation directory additionally separates work into:

```text
01_Structure
02_Functionality
03_Unit_Testing
```

This reflects the progression from **model design**, through **application behavior**, to **verification**.

## Getting Started

### Prerequisites

You will need:

- Python 3
- Git
- A Python IDE or editor such as PyCharm or Visual Studio Code

The exercises rely primarily on the **Python standard library** and do not require a large third-party dependency stack.

### Clone the Repository

```bash
git clone https://github.com/SimeonChifligarov/SoftUni_Python_OOP_Exams.git
cd SoftUni_Python_OOP_Exams
```

### Optional Virtual Environment

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows PowerShell

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
py -m venv .venv
.venv\Scripts\activate.bat
```

No external packages are required for the core OOP examples or Python's built-in `unittest` framework.

## Working with the Repository

These projects were originally designed around **SoftUni exam and judge conventions**, so they are best approached as educational source-code exercises rather than as a single installable application.

A useful learning workflow is:

1. Open one exam-preparation directory.
2. Study the class structure before reading the implementation.
3. Identify base classes and subclasses.
4. Inspect the validation rules.
5. Follow how objects interact with the main application/service class.
6. Reimplement parts of the project independently.
7. Compare your implementation with the repository solution.
8. Write additional unit tests for edge cases.
9. Refactor duplicated logic while preserving the required public interface.

> [!TIP]
> For OOP exam preparation, try rebuilding a project from the specification without looking at the completed solution. Use the existing implementation only afterward to compare architecture, validation, and edge-case handling.

## Educational Scope

This repository is intended for:

- Python OOP revision
- Exam preparation
- Studying class hierarchies
- Practicing inheritance and abstraction
- Reviewing encapsulation techniques
- Understanding multi-class application design
- Practicing validation and exception handling
- Learning Python unit testing
- Comparing alternative implementation approaches

It is **not** intended to be:

- A production bakery-management application
- An installable Python package
- A reusable public API
- A commercial software product
- A replacement for the official SoftUni course
- A source of ready-made submissions for active assignments or examinations

Some implementations intentionally follow the exact interface and structural constraints of the original educational tasks. Those constraints may differ from architecture that would be selected for a production system.

## Academic Integrity

If you are currently taking the corresponding course or working on similar assignments, use this repository responsibly.

The most effective approach is to:

- Attempt the problem independently first
- Use the code to review concepts after completing your own attempt
- Compare architecture rather than copying implementation
- Investigate why each validation rule exists
- Write your own additional tests
- Refactor solutions as a learning exercise

Do not submit code from this repository as your own work for an active assessment.

## SoftUni Attribution and Disclaimer

The exercises in this repository are based on material associated with:

**[Software University (SoftUni)](https://softuni.bg/)**  
Course area: **Python Object-Oriented Programming**

Credit for the original course materials, task descriptions, examination requirements, project skeletons, and supplied classes belongs to **SoftUni and the respective authors/rightsholders**.

This repository:

- Contains my personal implementations and solutions
- Is independently maintained
- Is not an official SoftUni repository
- Is not affiliated with or endorsed by SoftUni
- Does not replace the official course material
- Does not claim ownership of third-party examination descriptions or supplied task assets

Where original skeleton files or supplied class definitions are referenced, their original ownership remains unchanged.

## License

The original code in this repository is distributed under the terms of the [MIT License](LICENSE).

```text
MIT License

Copyright (c) 2022 Simeon Chifligarov
```

The MIT License applies to material for which the repository owner holds the necessary rights. It does not override the ownership, copyright, or licensing terms of third-party educational materials, exam descriptions, or project skeletons.

## Author

**Simeon Chifligarov**

- GitHub: [@SimeonChifligarov](https://github.com/SimeonChifligarov)
- Repository: [SoftUni Python OOP Exams](https://github.com/SimeonChifligarov/SoftUni_Python_OOP_Exams)

---

### If this repository helped you, consider giving it a star.

**Model objects carefully. Protect their state. Test their behavior.**
