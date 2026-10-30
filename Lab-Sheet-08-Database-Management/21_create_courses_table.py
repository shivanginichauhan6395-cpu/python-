# Program 21: Create the courses table and insert course data.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_name TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    """)
    courses = [
        (1, 1, "Python"),
        (2, 2, "Database Management"),
        (3, 3, "Cloud Computing"),
        (4, 4, "Web Development")
    ]
    cursor.executemany(
        "INSERT OR REPLACE INTO courses (course_id, student_id, course_name) VALUES (?, ?, ?)",
        courses
    )
    connection.commit()
    print("Courses table created and data inserted successfully.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
