# Flask Financial Alerts System

This project is initially set up as a basic user management system using Flask,
APIFlask, Flask-SQLAlchemy, and SQLite, serving as a starting point for building a proof
of concept for a more complex financial alerts system.

The provided user management features include creating users, retrieving a list of
users, and fetching users by their ID. Each user has an email, a password (hashed for
security), and an active status. Candidates are encouraged to expand upon this
foundation and integrate financial alert functionalities as needed.

## Features

- Basic user management with unique email addresses for user creation.
- Fetching user details by ID and listing all users with pagination.
- Secure password hashing.
- **Extendable for financial alert features.**

## Requirements

- Python 3.8+
- Flask
- APIFlask
- Flask-SQLAlchemy

## Installation

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies with `pip install -r requirements.txt`.
4. Run the server using `flask run --debugger --reload` for development with live
reloading.

## Notes

- The user management system is provided to minimize initial setup time and to allow
focus on implementing the financial alerts features.
- Feel free to modify or extend the existing codebase to suit the requirements of the
financial alerts system.
- `transactions.json` is provided as a sample data set for the financial alerts system.

