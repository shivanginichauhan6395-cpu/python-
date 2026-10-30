# Program 19: Find the student with highest marks
import sqlite3

try:
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS students
        (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER, marks REAL)""")
    cursor.execute("SELECT * FROM students ORDER BY marks DESC LIMIT 1")
    record = cursor.fetchone()

    if record:
        print("Student with highest marks:", record)
    else:
        print("No student records found.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
