# Program 29: Search for a student by name in a CSV file

import csv

try:
    search_name = input("Enter student name to search: ")

    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)
        found = False

        for row in reader:
            if row["Name"].lower() == search_name.lower():
                print("Record found:", row)
                found = True

        if not found:
            print("Student record not found.")
except FileNotFoundError:
    print("CSV file not found. Run Program 21 first.")
