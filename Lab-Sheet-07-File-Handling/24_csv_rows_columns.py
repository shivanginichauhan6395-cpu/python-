# Program 24: Count rows and columns in a CSV file

import csv

try:
    with open("students.csv", "r") as file:
        rows = list(csv.reader(file))

    if rows:
        print("Number of rows (excluding heading):", len(rows) - 1)
        print("Number of columns:", len(rows[0]))
    else:
        print("CSV file is empty.")
except FileNotFoundError:
    print("CSV file not found. Run Program 21 first.")
