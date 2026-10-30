# Program 9: Copy content from one file to another

try:
    source = open("data.txt", "r")
    content = source.read()
    source.close()

    destination = open("copy.txt", "w")
    destination.write(content)
    destination.close()

    print("File copied successfully.")
except FileNotFoundError:
    print("Source file not found. Run Program 1 first.")
