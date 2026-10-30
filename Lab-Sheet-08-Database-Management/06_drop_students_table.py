# Program 6: Drop (delete) the students table.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS students")
    connection.commit()
    print("Students table dropped successfully.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
