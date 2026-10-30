# Program 28: Display database errors using exception handling.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    # This query uses a table name that may not exist.
    cursor.execute("SELECT * FROM unknown_table")
    print(cursor.fetchall())
except sqlite3.Error as error:
    print("A database error occurred:", error)
finally:
    if connection:
        connection.close()
        print("Database connection closed.")
