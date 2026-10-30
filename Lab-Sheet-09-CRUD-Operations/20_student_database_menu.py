# Program 20: Menu-driven student CRUD application using SQLite
import sqlite3

def connect_db():
    connection = sqlite3.connect("student.db")
    connection.execute("""CREATE TABLE IF NOT EXISTS students
        (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER, marks REAL)""")
    connection.commit()
    return connection

while True:
    print("\n--- Student Database Menu ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")
    choice = input("Enter your choice: ")

    try:
        connection = connect_db()
        cursor = connection.cursor()

        if choice == "1":
            roll = int(input("Enter roll number: "))
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            marks = float(input("Enter marks: "))
            cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)",
                           (roll, name, age, marks))
            connection.commit()
            print("Student added successfully.")

        elif choice == "2":
            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(row)
            else:
                print("No records found.")

        elif choice == "3":
            roll = int(input("Enter roll number to search: "))
            cursor.execute("SELECT * FROM students WHERE id = ?", (roll,))
            row = cursor.fetchone()
            print(row if row else "Student not found.")

        elif choice == "4":
            roll = int(input("Enter roll number: "))
            marks = float(input("Enter new marks: "))
            cursor.execute("UPDATE students SET marks = ? WHERE id = ?", (marks, roll))
            connection.commit()
            print("Marks updated." if cursor.rowcount else "Student not found.")

        elif choice == "5":
            roll = int(input("Enter roll number to delete: "))
            cursor.execute("DELETE FROM students WHERE id = ?", (roll,))
            connection.commit()
            print("Record deleted." if cursor.rowcount else "Student not found.")

        elif choice == "6":
            print("Program closed.")
            connection.close()
            break

        else:
            print("Invalid choice. Please try again.")

        connection.close()

    except ValueError:
        print("Please enter valid numeric values.")
    except sqlite3.IntegrityError:
        print("This roll number already exists.")
    except sqlite3.Error as error:
        print("Database error:", error)
