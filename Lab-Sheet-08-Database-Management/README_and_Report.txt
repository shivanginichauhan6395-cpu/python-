MCA I Semester - Python Programming Lab (Lab Sheet 08)
Database Management using Python Programming

Solution details
----------------
- All 30 programs are solved in beginner-friendly Python.
- SQLite is used because sqlite3 is already included with Python 3.
- All programs use the common database file: student_db.db
- SQL values are passed with parameterized queries (?).
- Comments explain the main steps.
- Database connections are closed using finally blocks.

How to run
----------
1. Install Python 3.
2. Extract this ZIP file.
3. Open Command Prompt / Terminal in the extracted folder.
4. Run the setup programs first:
       python 02_create_database.py
       python 03_create_students_table.py
       python 09_insert_multiple_records.py
5. Run any other program, for example:
       python 10_display_all_records.py

Important notes
---------------
- Program 6 deletes the students table. Run Program 3 again after using it.
- Program 20 empties the students table. It keeps the table structure.
  SQLite does not support TRUNCATE TABLE, so DELETE is used instead.
- Programs 16, 17, 18 and 30 take input from the user.
- Program 27 expects a file named students.csv in the same folder.
  You can create it first by running Program 26.
- Program 21 creates the courses table. Programs 22 and 23 use that table.
- Run Program 3 and Program 9 before running student-data programs.

Files
-----
01 to 30: Individual Python program files.
