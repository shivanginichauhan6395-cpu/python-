# Program 11: Display only name and marks of students.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT name, marks FROM students")
    records = cursor.fetchall()

    for row in records:
        print("Name:", row[0], "| Marks:", row[1])
    if not records:
        print("No records found.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
