# Program 6: Display only even-numbered lines

try:
    file = open("data.txt", "r")
    for number, line in enumerate(file, start=1):
        if number % 2 == 0:
            print(line, end="")
    file.close()
except FileNotFoundError:
    print("File not found. Run Program 1 first.")
