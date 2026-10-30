# Program 7: Write multiple lines entered by the user into a file

file = open("user_lines.txt", "w")
print("Enter 3 lines:")
for i in range(3):
    line = input("Enter line: ")
    file.write(line + "\n")
file.close()

print("All lines saved successfully.")
