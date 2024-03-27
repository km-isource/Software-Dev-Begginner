# File Creation:
# Create a Python script (file_handling_assignment.py) that does the following:
# Creates a new text file named "my_file.txt" in write mode ('w').
# Write at least three lines of text to the file, including a mix of strings and numbers.


# File Reading and Display:
# Enhance your script to read the contents of "my_file.txt" and display them on the console.


# File Appending:
# Modify the script to open "my_file.txt" in append mode ('a').
# Append three additional lines of text to the existing content.


# Error Handling:
# Implement error handling using try, except, and finally blocks to manage potential file-related exceptions (e.g., FileNotFoundError, PermissionError).

try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line here\n")
except IOError as e:
    print("Error:", e)
else:
    print("File 'my_file.txt' created successfully.")

try:
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("Error: File 'my_file.txt' not found.")
except PermissionError:
    print("Error: Permission denied while trying to read the file.")


try:
    with open("my_file.txt", "a") as file:
        file.write("Appended line 1\n")
        file.write("67890\n")
        file.write("One more line appended\n")
except IOError as e:
    print("Error:", e)
else:
    print("Content appended to 'my_file.txt'.")


try:

    with open("non_existent_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: File 'non_existent_file.txt' not found.")
except PermissionError:
    print("Error: Permission denied while trying to read the file.")
finally:
    print("This block is always executed, regardless of any exceptions.")
