# Program 16: Update a student's marks using their ID.
import sqlite3

connection = None
try:
    student_id = int(input("Enter student ID: "))
    new_marks = float(input("Enter new marks: "))

    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE students SET marks=? WHERE id=?",
        (new_marks, student_id)
    )
    connection.commit()

    if cursor.rowcount:
        print("Student marks updated successfully.")
    else:
        print("Student ID not found.")
except ValueError:
    print("Please enter a valid number.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
