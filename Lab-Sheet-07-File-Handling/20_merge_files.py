# Program 20: Merge two text files into a third file

try:
    file1 = open("data.txt", "r")
    content1 = file1.read()
    file1.close()

    file2 = open("second.txt", "r")
    content2 = file2.read()
    file2.close()

    output = open("merged.txt", "w")
    output.write(content1 + "\n" + content2)
    output.close()

    print("Both files merged into merged.txt.")
except FileNotFoundError:
    print("Create data.txt and second.txt before running this program.")
