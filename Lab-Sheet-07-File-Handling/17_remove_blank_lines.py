# Program 17: Remove blank lines from a file

try:
    file = open("data.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("clean_data.txt", "w")
    for line in lines:
        if line.strip():
            file.write(line)
    file.close()

    print("Blank lines removed. Result saved in clean_data.txt.")
except FileNotFoundError:
    print("File not found. Run Program 1 first.")
