# Program 4: Display the structure of the students table.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()
    cursor.execute("PRAGMA table_info(students)")
    columns = cursor.fetchall()

    if columns:
        print("Structure of students table:")
        for column in columns:
            print("Column:", column[1], "| Type:", column[2],
                  "| Primary key:", column[5])
    else:
        print("Students table does not exist.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
