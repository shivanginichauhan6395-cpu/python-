# Program 1: Create a list of student records

students = []

n = int(input("How many students do you want to add? "))

for i in range(n):
    print("\nEnter details of student", i + 1)
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    # Store one student's details in a dictionary
    student = {"roll": roll, "name": name, "age": age, "marks": marks}
    students.append(student)

print("\nStudent records created successfully.")
print(students)
