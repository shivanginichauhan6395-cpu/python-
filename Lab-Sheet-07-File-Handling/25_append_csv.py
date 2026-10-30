# Program 25: Append a new student record to a CSV file

import csv
import os

file_exists = os.path.exists("students.csv")

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(["Name", "Marks", "Age"])

    name = input("Enter student name: ")
    marks = input("Enter marks: ")
    age = input("Enter age: ")
    writer.writerow([name, marks, age])

print("New record added successfully.")
