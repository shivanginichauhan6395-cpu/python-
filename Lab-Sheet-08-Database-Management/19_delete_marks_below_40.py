# Program 19: Delete all students who scored below 40 marks.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students WHERE marks < ?", (40,))
    connection.commit()
    print(cursor.rowcount, "student record(s) deleted.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
