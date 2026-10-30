# Program 12: Display students who scored more than 80 marks.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE marks > ?", (80,))
    records = cursor.fetchall()

    for row in records:
        print(row)
    if not records:
        print("No student scored more than 80.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
