# employee-management-system
This is a Python-based employee management system that allows users to manage employee data stored in a local text file (22100011016.txt). The application provides a command-line menu to perform various operations such as adding, deleting, updating, and searching for employees, as well as calculating salary raise percentages.

Features
Add a new employee

Delete an employee by ID

Search for an employee by ID

Update employee information

Calculate salary raise percentage

Find the employee with the highest raise

Data Storage (Text File Usage)
All employee records are stored in a file named 22100011016.txt.
Each line in the file represents one employee, and fields are separated by hyphens (-):

Name-Surname-ID-Age-NumberOfChildren-OldSalary-NewSalary
Example:
Ali-Kaya-101-35-2-10000-12000
Ayse-Demir-102-29-0-9500-10500

The file is appended when adding a new employee.

It is rewritten when an employee is deleted or updated.

All calculations and lookups are done using this file.

How to Run the Program
Make sure Python is installed on your system (version 3.x).

Run the script in a terminal or command prompt:
python your_script_name.py
Use the menu to perform actions. The file 22100011016.txt will be created automatically in the same directory.

Note
Input validation is included (for example, the program will re-ask for correct input type if a number is expected).

Employee ID must be unique and is used to identify and manage records.

