# Program 3: Read a file one line at a time

try:
    file = open("data.txt", "r")
    for line in file:
        print(line, end="")
    file.close()
except FileNotFoundError:
    print("File not found. Run Program 1 first.")
