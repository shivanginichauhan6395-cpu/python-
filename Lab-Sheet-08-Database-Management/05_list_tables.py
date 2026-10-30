# Program 5: List all tables in the database.
import sqlite3

connection = None
try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT name FROM sqlite_master
        WHERE type='table' AND name NOT LIKE 'sqlite_%'
    """)
    tables = cursor.fetchall()

    print("Tables in the database:")
    if tables:
        for table in tables:
            print(table[0])
    else:
        print("No tables found.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
