# employee-management-system
This is a Python-based employee management system that allows users to manage employee data stored in a local text file (`22100011016.txt`). The program provides a menu-based interface for the following operations:

## Features

- Add a new employee  
- Delete an employee by ID  
- Search for an employee by ID  
- Update employee information  
- Calculate salary raise percentage  
- Find the employee with the highest raise  

## Data Storage: `22100011016.txt`

All employee records are stored in a plain text file named `22100011016.txt`.

Each line in the file represents **one employee**, and fields are separated by hyphens (`-`):

Name-Surname-ID-Age-NumberOfChildren-OldSalary-NewSalary

**Example:**
Ali-Kaya-101-35-2-10000-12000
Ayse-Demir-102-29-0-9500-10500


- When a new employee is added, a new line is appended.
- When an employee is deleted or updated, the entire file is rewritten.
- All calculations and searches use this file as the data source.

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Save the script and place it in a folder. You don’t need to manually create the `.txt` file — it will be created automatically.
3. Open a terminal or command prompt in that folder.
4. Run the program using the following command:

python employeeManagement.py


## Notes

- Input validation is included. For example, if a number is expected but a string is entered, the program will ask again.
- Each employee must have a **unique ID**.




