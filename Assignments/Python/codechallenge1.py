




# 1 Write a program that accepts user input to create a list of integers.
# Then, compute the sum of all the integers in the list.

user_input = []
for i in range (5):
    integer = int(input("Enter a Number: "))
    user_input.append(integer)

print(user_input)
print(sum(user_input))



# 2 Create a tuple containing the names of five of your favorite books. 
# Then, use a for loop to print each book name on a separate line.

books = ('English', 'Kiswahili', 'Maths', 'Science', 'Comm Skills')
for book in books:
    print(book)



# 3 Write a program that uses a dictionary to store information about a person,
# such as their name, age, and favorite color.
# Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.

personal_info ={}

personal_info['Name'] = input("Enter Your Name: ")
personal_info['Location'] = input("Enter Your Location: ")
personal_info['Age'] = int(input("Enter Your Age: "))
print(personal_info)


    
# 4 Write a program that accepts user input to create two sets of integers.
# Then, create a new set that contains only the elements that are common to both sets.

set1 = set(map(int, input("Enter 3 Intergers Separated by spaces : ").split()))
set2 = set(map(int, input("Enter The 2nd Set Separated by Spaces: ").split()))

common_intergers = set1.intersection(set2)
print(common_intergers)


# 5 Create a program that stores a list of words. \
# Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

words = ["hello", "world", "how", "are", "you", "today"]

odd_length_words = [word for word in words if len(word) % 2 != 0]

print("Original list:", words)
print("Words with odd length:", odd_length_words)
