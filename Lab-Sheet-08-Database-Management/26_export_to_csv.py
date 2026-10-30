# Program 26: Export student table data into a CSV file.
import sqlite3
import csv

connection = None
try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "age", "marks"])
        writer.writerows(records)

    print("Student data exported to students.csv successfully.")
except (sqlite3.Error, OSError) as error:
    print("Error:", error)
finally:
    if connection:
        connection.close()
