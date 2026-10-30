# Program 10: CRUD operations using a text file

FILE_NAME = "student_records.txt"

def add_record():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    marks = input("Enter marks: ")
    with open(FILE_NAME, "a") as file:
        file.write(f"{roll},{name},{age},{marks}\n")
    print("Record added.")

def view_records():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()
        if not records:
            print("No records found.")
        for record in records:
            print(record.strip())
    except FileNotFoundError:
        print("File not found. Add a record first.")

def update_record():
    roll = input("Enter roll number to update: ")
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()
        updated = False
        with open(FILE_NAME, "w") as file:
            for record in records:
                data = record.strip().split(",")
                if data[0] == roll:
                    name = input("Enter new name: ")
                    age = input("Enter new age: ")
                    marks = input("Enter new marks: ")
                    file.write(f"{roll},{name},{age},{marks}\n")
                    updated = True
                else:
                    file.write(record)
        print("Record updated." if updated else "Record not found.")
    except FileNotFoundError:
        print("File not found.")

def delete_record():
    roll = input("Enter roll number to delete: ")
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()
        remaining = [r for r in records if r.strip().split(",")[0] != roll]
        with open(FILE_NAME, "w") as file:
            file.writelines(remaining)
        print("Record deleted." if len(remaining) < len(records) else "Record not found.")
    except FileNotFoundError:
        print("File not found.")

while True:
    print("\n1. Add  2. View  3. Update  4. Delete  5. Exit")
    choice = input("Enter choice: ")
    try:
        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            update_record()
        elif choice == "4":
            delete_record()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
    except OSError as error:
        print("File error:", error)
