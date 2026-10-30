# Program 15: Update student marks using roll number
import sqlite3

try:
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS students
        (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER, marks REAL)""")
    roll = int(input("Enter roll number: "))
    marks = float(input("Enter new marks: "))
    cursor.execute("UPDATE students SET marks = ? WHERE id = ?", (marks, roll))
    connection.commit()

    if cursor.rowcount > 0:
        print("Marks updated successfully.")
    else:
        print("Student not found.")
except ValueError:
    print("Please enter valid numbers.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
