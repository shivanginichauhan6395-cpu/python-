# Program 4: Count the number of words in a text file

try:
    file = open("data.txt", "r")
    content = file.read()
    words = content.split()
    print("Total words:", len(words))
    file.close()
except FileNotFoundError:
    print("File not found. Run Program 1 first.")
