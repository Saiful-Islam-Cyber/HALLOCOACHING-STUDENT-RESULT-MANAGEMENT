# HALLO COACHING STUDENT RESULT MANAGEMENT

A robust, terminal-based Python application designed to manage student academic records, automate performance diagnostics, and persist data across runtimes using flat-file CSV storage.

## Architectural Design
The application is structured into modular components to adhere to clean coding standards and the Single Responsibility Principle:
- `cond.py`: Handles individual conditional decision boundaries (Grades and Pass/Fail resolution).
- `oop.py`: Encapsulates object-oriented structures (`Student` data models and the `ResultManager` array controller).
- `list.py`: Serves as the primary operational entry point, controlling application loops, I/O streams, and terminal runtime validation.

## Installation & Deployment
1. Ensure a working distribution of **Python 3.x** is installed on your local machine.
2. Clone or open this repository directory folder.
3. Open your terminal pointing to this path and activate your local environment.

## Running the Application
To start the program interface, run the entry point file from your terminal:
```bash
python list.py
```
