# API Automation Framework

## Overview

This project is a simple API Automation Framework built using Python, Pytest, and Requests. It is designed to automate REST API testing using reusable HTTP methods, external test data, fixtures, and HTML reporting.

The framework follows a modular structure that separates test logic, test data, and API utilities, making the code easier to maintain and extend.


## Features

* GET API Testing
* POST API Testing
* PUT API Testing
* DELETE API Testing
* Reusable API Client
* JSON-Based Test Data Management
* Pytest Fixtures
* Dynamic Test Data Generation
* Automated HTML Reports

## Project Structure

api-automation-framework/
│
├── tests/
│   └── test_getuser.py
│
├── utils/
│   └── apis.py
│
├── data/
│   └── test_data.json
│
├── reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── .gitignore

## Tech Stack

* Python
* Pytest
* Requests
* Pytest HTML
* JSON

## Test Coverage

### User API Tests

* Validate User Retrieval
* Create User
* Update User
* Delete User


## Running Tests
pytest

Generate HTML reports:
pytest -v

## Concepts Implemented

* API Automation
* Pytest Fixtures
* Data-Driven Testing
* JSON Test Data Management
* Reusable API Methods
* Assertions and Validations
* HTML Reporting

## Future Enhancements

* Authentication Testing
* Logging
* CI/CD Integration
* GitHub Actions
* Jenkins Integration
* Environment Management

## Author

Built as part of learning API Automation Testing using Python and Pytest.

