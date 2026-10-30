# Program 17: Update the name of a student using their ID.
import sqlite3

connection = None
try:
    student_id = int(input("Enter student ID: "))
    new_name = input("Enter new name: ")

    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE students SET name=? WHERE id=?",
        (new_name, student_id)
    )
    connection.commit()

    if cursor.rowcount:
        print("Student name updated successfully.")
    else:
        print("Student ID not found.")
except ValueError:
    print("Please enter a valid ID.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
