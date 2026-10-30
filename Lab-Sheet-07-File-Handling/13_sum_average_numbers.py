# Program 13: Read numbers from a file and find sum and average

try:
    file = open("numbers.txt", "r")
    numbers = [float(value) for value in file.read().split()]
    file.close()

    if len(numbers) > 0:
        print("Sum =", sum(numbers))
        print("Average =", sum(numbers) / len(numbers))
    else:
        print("No numbers found in the file.")
except FileNotFoundError:
    print("Create a file named numbers.txt and enter numbers separated by spaces.")
except ValueError:
    print("Please keep only numbers in numbers.txt.")
