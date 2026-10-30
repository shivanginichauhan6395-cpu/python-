# Program 18: Delete a student record using ID.
import sqlite3

connection = None
try:
    student_id = int(input("Enter student ID to delete: "))
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    connection.commit()

    if cursor.rowcount:
        print("Student record deleted successfully.")
    else:
        print("Student ID not found.")
except ValueError:
    print("Please enter a valid ID.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
