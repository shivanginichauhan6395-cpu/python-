# Program 2: Display all student records

students = [
    {"roll": "101", "name": "Aman", "age": 20, "marks": 85},
    {"roll": "102", "name": "Riya", "age": 19, "marks": 90}
]

# Check whether the list contains records
if len(students) == 0:
    print("No student record found.")
else:
    print("Student Records")
    for student in students:
        print("Roll:", student["roll"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Marks:", student["marks"])
        print("--------------------")
