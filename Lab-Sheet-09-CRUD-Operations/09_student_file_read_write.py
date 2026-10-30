# Program 9: Save student data in a text file and read it back

try:
    n = int(input("How many students? "))

    # Write student details into a text file
    with open("students.txt", "w") as file:
        for i in range(n):
            print("\nStudent", i + 1)
            roll = input("Roll number: ")
            name = input("Name: ")
            age = input("Age: ")
            marks = input("Marks: ")
            file.write(roll + "," + name + "," + age + "," + marks + "\n")

    print("\nData saved successfully.")

    # Read and display the saved data
    print("\nStudent records from file:")
    with open("students.txt", "r") as file:
        for line in file:
            print(line.strip())

except ValueError:
    print("Please enter a valid number.")
except OSError as error:
    print("File error:", error)
