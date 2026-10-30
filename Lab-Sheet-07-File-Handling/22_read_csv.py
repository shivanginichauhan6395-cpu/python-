# Program 22: Read and display data from a CSV file

import csv

try:
    with open("students.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("CSV file not found. Run Program 21 first.")
