# Program 15: Replace one word with another word in a file

try:
    file = open("data.txt", "r")
    content = file.read()
    file.close()

    old_word = input("Enter word to replace: ")
    new_word = input("Enter new word: ")
    content = content.replace(old_word, new_word)

    file = open("data.txt", "w")
    file.write(content)
    file.close()
    print("Word replaced successfully.")
except FileNotFoundError:
    print("File not found. Run Program 1 first.")
