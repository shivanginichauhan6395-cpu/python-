# Program 28: Find the student with the highest marks in a CSV file

import csv

try:
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)
        students = list(reader)

    if students:
        highest = max(students, key=lambda student: float(student["Marks"]))
        print("Student with highest marks:", highest["Name"])
        print("Highest marks:", highest["Marks"])
    else:
        print("No student records found.")
except FileNotFoundError:
    print("CSV file not found. Run Program 21 first.")
except (KeyError, ValueError):
    print("Check the Marks column in the CSV file.")
