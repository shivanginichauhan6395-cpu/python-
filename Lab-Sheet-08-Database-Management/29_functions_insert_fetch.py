# Program 29: Use functions to insert and fetch student data.
import sqlite3

def insert_student(connection, student):
    # Insert one student using a parameterized query.
    cursor = connection.cursor()
    cursor.execute(
        "INSERT OR REPLACE INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)",
        student
    )
    connection.commit()
    print("Student inserted successfully.")

def fetch_students(connection):
    # Fetch and display all student records.
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

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
    insert_student(connection, (10, "Karan", 21, 81))
    print("Student records:")
    fetch_students(connection)
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
