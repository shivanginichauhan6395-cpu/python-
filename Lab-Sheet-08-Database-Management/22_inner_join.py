# Program 22: Perform INNER JOIN between students and courses.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT students.name, courses.course_name
        FROM students
        INNER JOIN courses ON students.id = courses.student_id
    """)
    records = cursor.fetchall()

    print("Student Name | Course")
    for row in records:
        print(row[0], "|", row[1])
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
