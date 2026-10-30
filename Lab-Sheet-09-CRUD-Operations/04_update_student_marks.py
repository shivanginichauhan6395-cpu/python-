# Program 4: Update a student's marks

students = [
    {"roll": "101", "name": "Aman", "age": 20, "marks": 85},
    {"roll": "102", "name": "Riya", "age": 19, "marks": 90}
]

roll = input("Enter roll number: ")
found = False

for student in students:
    if student["roll"] == roll:
        try:
            new_marks = float(input("Enter new marks: "))
            student["marks"] = new_marks
            print("Marks updated successfully.")
            print(student)
        except ValueError:
            print("Please enter marks in numbers.")
        found = True
        break

if not found:
    print("Student not found.")
