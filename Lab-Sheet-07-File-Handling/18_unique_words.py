# Program 18: Save only unique words into another file

try:
    file = open("data.txt", "r")
    words = file.read().split()
    file.close()

    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    output = open("unique_words.txt", "w")
    output.write(" ".join(unique_words))
    output.close()

    print("Unique words saved in unique_words.txt.")
except FileNotFoundError:
    print("File not found. Run Program 1 first.")
