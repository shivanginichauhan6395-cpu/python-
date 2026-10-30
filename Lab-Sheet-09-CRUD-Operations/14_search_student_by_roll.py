# Program 14: Search a student using roll number
import sqlite3

try:
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS students
        (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER, marks REAL)""")
    roll = int(input("Enter roll number to search: "))
    cursor.execute("SELECT * FROM students WHERE id = ?", (roll,))
    record = cursor.fetchone()

    if record:
        print("Student found:", record)
    else:
        print("Student not found.")
except ValueError:
    print("Roll number must be a number.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
