# Program 8: Insert one student record.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY, name TEXT NOT NULL,
            age INTEGER, marks REAL
        )
    """)
    cursor.execute(
        "INSERT OR REPLACE INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)",
        (1, "Aman", 20, 85.5)
    )
    connection.commit()
    print("One student record inserted successfully.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
