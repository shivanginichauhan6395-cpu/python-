# Program 20: Empty the table but keep its structure.
# SQLite does not support the TRUNCATE TABLE command, so DELETE is used.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students")
    connection.commit()
    print("Students table is now empty. Its structure is unchanged.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
