# Program 11: Connect to SQLite and create students table
import sqlite3

try:
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            marks REAL
        )
    """)
    connection.commit()
    print("Students table created successfully.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
