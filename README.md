# Student Management Functions (Simple Guide)
This code is a small system to manage students using a list (inventory). You can add, search, update, and delete students.
🔹 ##Main Functions
*ask_name()*
Asks the user to type a student name.
It only accepts letters (no numbers).

*ask_age()*
*Asks for the student’s age.*
It must be a number greater than 0.

*ask_course()*
Asks for the student’s course.

*student_state()*
Asks if the student is "active" or "inactive".
If the input is wrong, it shows an error.

*Data Handling*
register_new_student(ID, Name, Age, Course, State)
Creates a dictionary (student object) with all the data.
Operations

*check_list(inventory)*
Shows all students.
If the list is empty, it prints a message.

*search_student(inventory, search)*
Searches a student by name or ID.
If found, it prints the student info.

*update_student(inventory, ID, Name, Age, Course, State)*
Updates a student’s data using the ID.

*delete_student(inventory, ID)*
Removes a student from the list using the ID.

*starting()*
Shows a simple countdown (3, 2, 1).

*clean_screen()*
Clears the terminal screen.


wrote by:
Maryuris Aragón
