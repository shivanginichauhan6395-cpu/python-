# Program 5: Count lines and characters in a file

try:
    file = open("data.txt", "r")
    content = file.read()
    lines = content.splitlines()
    print("Total lines:", len(lines))
    print("Total characters:", len(content))
    file.close()
except FileNotFoundError:
    print("File not found. Run Program 1 first.")
