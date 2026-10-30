# Program 13: Display students in descending order of marks.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students ORDER BY marks DESC")
    for row in cursor.fetchall():
        print(row)
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
