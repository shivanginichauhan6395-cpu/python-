# Program 14: Display the longest line in a file

try:
    file = open("data.txt", "r")
    lines = file.readlines()
    file.close()

    if lines:
        longest = max(lines, key=len)
        print("Longest line:", longest)
    else:
        print("File is empty.")
except FileNotFoundError:
    print("File not found. Run Program 1 first.")
