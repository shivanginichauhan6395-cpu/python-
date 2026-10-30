# Program 9: Insert multiple student records.
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
    students = [
        (1, "Aman", 20, 85.5),
        (2, "Riya", 21, 92),
        (3, "Rahul", 19, 76),
        (4, "Neha", 20, 88)
    ]
    cursor.executemany(
        "INSERT OR REPLACE INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)",
        students
    )
    connection.commit()
    print(len(students), "records inserted successfully.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
