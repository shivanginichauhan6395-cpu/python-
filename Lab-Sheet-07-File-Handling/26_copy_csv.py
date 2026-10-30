# Program 26: Copy data from one CSV file to another

import csv

try:
    with open("students.csv", "r", newline="") as source:
        rows = list(csv.reader(source))

    with open("students_copy.csv", "w", newline="") as destination:
        writer = csv.writer(destination)
        writer.writerows(rows)

    print("CSV data copied to students_copy.csv.")
except FileNotFoundError:
    print("CSV file not found. Run Program 21 first.")
