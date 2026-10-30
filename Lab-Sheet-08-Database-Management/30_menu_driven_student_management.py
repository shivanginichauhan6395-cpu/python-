# Program 30: Simple menu-driven student management application.
import sqlite3

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
    connection.commit()

    while True:
        print("\n--- Student Management ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student Marks")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = int(input("Enter ID: "))
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            marks = float(input("Enter marks: "))
            cursor.execute(
                "INSERT OR REPLACE INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)",
                (student_id, name, age, marks)
            )
            connection.commit()
            print("Student added successfully.")

        elif choice == "2":
            cursor.execute("SELECT * FROM students")
            records = cursor.fetchall()
            for row in records:
                print(row)
            if not records:
                print("No student records found.")

        elif choice == "3":
            student_id = int(input("Enter student ID: "))
            marks = float(input("Enter new marks: "))
            cursor.execute(
                "UPDATE students SET marks=? WHERE id=?",
                (marks, student_id)
            )
            connection.commit()
            print("Record updated." if cursor.rowcount else "Student ID not found.")

        elif choice == "4":
            student_id = int(input("Enter student ID to delete: "))
            cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
            connection.commit()
            print("Record deleted." if cursor.rowcount else "Student ID not found.")

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")

except ValueError:
    print("Please enter valid numeric values.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
        print("Database connection closed.")
