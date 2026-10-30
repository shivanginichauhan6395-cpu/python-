# Program 15: Display the top three students according to marks.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students ORDER BY marks DESC LIMIT 3")
    records = cursor.fetchall()

    print("Top 3 students:")
    for row in records:
        print(row)
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
