# employee-management-system
This is a Python-based employee management system that allows users to manage employee data stored in a local text file (22100011016.txt). The application provides a menu-based interface to perform the following operations:

Features
Add a new employee

Delete an employee by ID

Search for an employee by ID

Update employee information

Calculate salary raise percentage

Find the employee with the highest raise

Data Storage: 22100011016.txt
All employee records are stored in a text file named 22100011016.txt.

Each line in the file represents one employee.

Fields are separated by hyphens (-).

The format of each line is as follows:
Name-Surname-ID-Age-NumberOfChildren-OldSalary-NewSalary
Example:
Ali-Kaya-101-35-2-10000-12000
Ayse-Demir-102-29-0-9500-10500
The file is updated automatically whenever an employee is added, deleted, or modified.

How to Run the Program
Make sure you have Python 3.x installed on your computer.

Save the project Python script in the same folder as 22100011016.txt (or let the program create the file).

Open a terminal or command prompt and run the script using:
python your_script_name.py
Follow the menu instructions displayed in the terminal.

Notes
The program includes input validation. For example, if a number is expected, the program will prompt the user again if the input is incorrect.

Each employee must have a unique ID, which is used to identify them in all operations.



