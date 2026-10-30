# Program 3: Search a student by name

students = [
    {"roll": "101", "name": "Aman", "age": 20, "marks": 85},
    {"roll": "102", "name": "Riya", "age": 19, "marks": 90},
    {"roll": "103", "name": "Karan", "age": 20, "marks": 78}
]

search_name = input("Enter student name to search: ").strip()
found = False

for student in students:
    if student["name"].lower() == search_name.lower():
        print("Student found:", student)
        found = True

if not found:
    print("Student not found.")
