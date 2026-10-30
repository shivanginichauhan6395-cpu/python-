# Program 24: Find the average marks of all students.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT AVG(marks) FROM students")
    average = cursor.fetchone()[0]

    if average is not None:
        print("Average marks:", round(average, 2))
    else:
        print("No student records available.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
