# Create an empty list called my_list.
# Append the following elements to my_list: 10, 20, 30, 40.
# Insert the value 15 at the second position in the list.
# Extend my_list with another list: [50, 60, 70].
# Remove the last element from my_list.
# Sort my_list in ascending order.
# Find and print the index of the value 30 in my_list.

my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

my_list.insert(1, 15)
print()
print("15 Inserted at 2nd Place")
print(my_list)

my_list.extend([50, 60, 70])
print()
print("50, 60, 70 Added To The List")
print(my_list)

my_list.pop()
print()
print('The Last No. 70 Is Removed')
print(my_list)

my_list.sort()
index = my_list.index(30)

print(my_list)
print(f"The index of 30 is: {index}")
