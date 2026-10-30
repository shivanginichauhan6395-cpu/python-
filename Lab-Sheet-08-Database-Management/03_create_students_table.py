# Program 3: Create the students table.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("student_db.db")
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
    if connection:
        connection.close()
