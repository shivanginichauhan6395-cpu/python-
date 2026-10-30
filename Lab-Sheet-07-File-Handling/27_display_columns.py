# Program 27: Display only Name and Marks columns from a CSV file

import csv

try:
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("Name:", row["Name"], "Marks:", row["Marks"])
except FileNotFoundError:
    print("CSV file not found. Run Program 21 first.")
except KeyError:
    print("Required columns are not available.")
