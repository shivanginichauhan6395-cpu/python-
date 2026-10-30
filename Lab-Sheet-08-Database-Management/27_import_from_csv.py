# Program 27: Import student records from students.csv into the database.
import sqlite3
import csv

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

    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = [
            (int(row["id"]), row["name"], int(row["age"]), float(row["marks"]))
            for row in reader
        ]

    cursor.executemany(
        "INSERT OR REPLACE INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)",
        rows
    )
    connection.commit()
    print(len(rows), "record(s) imported successfully.")
except (sqlite3.Error, OSError, ValueError, KeyError) as error:
    print("Error:", error)
finally:
    if connection:
        connection.close()
