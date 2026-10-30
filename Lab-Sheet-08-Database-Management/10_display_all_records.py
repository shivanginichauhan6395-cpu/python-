# Program 10: Read and display all student records.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    print("ID  Name  Age  Marks")
    for row in records:
        print(row)
    if not records:
        print("No records found.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
