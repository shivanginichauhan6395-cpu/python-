# Program 21: Create a CSV file and write student data

import csv

students = [
    ["Name", "Marks", "Age"],
    ["Aman", 85, 20],
    ["Riya", 90, 21],
    ["Karan", 78, 20]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file created successfully.")
