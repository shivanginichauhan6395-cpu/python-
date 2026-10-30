# Program 19: Sort all words alphabetically and save them

try:
    file = open("data.txt", "r")
    words = file.read().split()
    file.close()

    words.sort(key=str.lower)

    output = open("sorted_words.txt", "w")
    output.write(" ".join(words))
    output.close()

    print("Sorted words saved in sorted_words.txt.")
except FileNotFoundError:
    print("File not found. Run Program 1 first.")
