# Program 2: Create a new SQLite database.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("student_db.db")
    print("Database student_db.db created successfully!")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
