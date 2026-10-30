# Program 30: Combine two CSV files into one CSV file

import csv

try:
    with open("students.csv", "r", newline="") as file1:
        rows1 = list(csv.reader(file1))

    with open("more_students.csv", "r", newline="") as file2:
        rows2 = list(csv.reader(file2))

    with open("all_students.csv", "w", newline="") as output:
        writer = csv.writer(output)
        if rows1:
            writer.writerows(rows1)
            writer.writerows(rows2[1:] if rows2 else [])

    print("CSV files combined into all_students.csv.")
except FileNotFoundError:
    print("Create students.csv and more_students.csv before running this program.")
