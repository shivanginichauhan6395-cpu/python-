# Program 11: Search for a particular word in a file

try:
    file = open("data.txt", "r")
    content = file.read()
    file.close()

    word = input("Enter the word to search: ")
    if word.lower() in content.lower().split():
        print("Word found in the file.")
    else:
        print("Word not found.")
except FileNotFoundError:
    print("File not found. Run Program 1 first.")
