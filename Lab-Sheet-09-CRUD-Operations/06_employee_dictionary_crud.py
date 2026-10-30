# Program 6: CRUD operations on employee dictionary

employees = {}

while True:
    print("\n1. Add  2. View  3. Update  4. Delete  5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        salary = input("Enter salary: ")
        employees[emp_id] = {"name": name, "salary": salary}
        print("Employee added successfully.")

    elif choice == "2":
        if employees:
            for emp_id, details in employees.items():
                print(emp_id, details)
        else:
            print("No employee records found.")

    elif choice == "3":
        emp_id = input("Enter employee ID to update: ")
        if emp_id in employees:
            employees[emp_id]["name"] = input("Enter new name: ")
            employees[emp_id]["salary"] = input("Enter new salary: ")
            print("Employee updated successfully.")
        else:
            print("Employee not found.")

    elif choice == "4":
        emp_id = input("Enter employee ID to delete: ")
        if emp_id in employees:
            del employees[emp_id]
            print("Employee deleted successfully.")
        else:
            print("Employee not found.")

    elif choice == "5":
        print("Program closed.")
        break
    else:
        print("Invalid choice. Try again.")
