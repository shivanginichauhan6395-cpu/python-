# Program 5: Delete a student by roll number

students = [
    {"roll": "101", "name": "Aman", "age": 20, "marks": 85},
    {"roll": "102", "name": "Riya", "age": 19, "marks": 90}
]

roll = input("Enter roll number to delete: ")
old_length = len(students)

students = [student for student in students if student["roll"] != roll]

if len(students) < old_length:
    print("Student record deleted successfully.")
else:
    print("Student not found.")

print("Remaining records:", students)
