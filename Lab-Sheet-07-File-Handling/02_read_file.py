# Program 2: Read the complete content of a text file

try:
    file = open("data.txt", "r")
    content = file.read()
    print("File content:")
    print(content)
    file.close()
except FileNotFoundError:
    print("File not found. Run Program 1 first.")
