# Program 16: Display the first and last lines of a file

try:
    file = open("data.txt", "r")
    lines = file.readlines()
    file.close()

    if lines:
        print("First line:", lines[0].strip())
        print("Last line:", lines[-1].strip())
    else:
        print("File is empty.")
except FileNotFoundError:
    print("File not found. Run Program 1 first.")
