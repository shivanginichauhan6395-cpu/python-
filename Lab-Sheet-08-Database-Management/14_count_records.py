# Program 14: Count the total number of student records.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM students")
    total = cursor.fetchone()[0]
    print("Total number of students:", total)
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
