# Program 10: Read a file and display its content in uppercase

try:
    file = open("data.txt", "r")
    content = file.read()
    file.close()
    print(content.upper())
except FileNotFoundError:
    print("File not found. Run Program 1 first.")
