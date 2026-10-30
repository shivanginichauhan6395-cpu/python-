# Program 13: Read and display all student records
import sqlite3

try:
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS students
        (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER, marks REAL)""")
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    if records:
        for row in records:
            print("Roll:", row[0], "Name:", row[1], "Age:", row[2], "Marks:", row[3])
    else:
        print("No student records found.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
