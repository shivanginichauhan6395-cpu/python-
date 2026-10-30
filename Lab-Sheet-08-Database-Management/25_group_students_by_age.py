# Program 25: Group students by age and count students in each group.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT age, COUNT(*) FROM students
        GROUP BY age ORDER BY age
    """)
    records = cursor.fetchall()

    print("Age | Number of students")
    for row in records:
        print(row[0], "|", row[1])
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
