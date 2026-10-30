# Program 23: Calculate the average of numeric columns in a CSV file

import csv

try:
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)
        marks = []
        ages = []

        for row in reader:
            marks.append(float(row["Marks"]))
            ages.append(float(row["Age"]))

    if marks:
        print("Average Marks:", sum(marks) / len(marks))
        print("Average Age:", sum(ages) / len(ages))
    else:
        print("No records found.")
except FileNotFoundError:
    print("CSV file not found. Run Program 21 first.")
except (KeyError, ValueError):
    print("Check the CSV column names and numeric values.")
