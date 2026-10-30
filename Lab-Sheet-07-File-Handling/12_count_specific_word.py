# Program 12: Count how many times a word occurs in a file

try:
    file = open("data.txt", "r")
    content = file.read()
    file.close()

    word = input("Enter the word: ")
    count = content.lower().split().count(word.lower())
    print("Occurrence of word:", count)
except FileNotFoundError:
    print("File not found. Run Program 1 first.")
