# Program 1: Connect to the SQLite database and display a message.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("student_db.db")
    print("Database connected successfully!")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
        print("Connection closed.")
