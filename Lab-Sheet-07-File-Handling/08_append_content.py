# Program 8: Append new content to an existing file

try:
    file = open("data.txt", "a")
    new_text = input("Enter text to add: ")
    file.write("\n" + new_text)
    file.close()
    print("New content added successfully.")
except OSError:
    print("There was a problem while writing the file.")
