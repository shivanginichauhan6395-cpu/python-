# Program 12: Insert a new student record
import sqlite3

try:
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS students
        (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER, marks REAL)""")

    roll = int(input("Enter roll number: "))
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    cursor.execute("INSERT INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)",
                   (roll, name, age, marks))
    connection.commit()
    print("Student record inserted successfully.")
except ValueError:
    print("Please enter valid numeric values.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
