x = 42
print(type(x))  # Prints <class 'int'>
print(id(x))  # Prints the unique identifier

x=20
print(id(x))

ls=[2,3,4]
ds=[10,20,30]
print(sum(ls))


print('*'*40)

#STRING Functions:
# String Functions Example

# Define a sample string
sample_string = "   Hello, World!   "

# Strip whitespace from both ends of the string
stripped_string = sample_string.strip()
print("Stripped:", stripped_string)  # Output: "Hello, World!"

# Convert the string to lowercase
lowercase_string = sample_string.lower()
print("Lowercase:", lowercase_string)  # Output: "   hello, world!   "

# Convert the string to uppercase
uppercase_string = sample_string.upper()
print("Uppercase:", uppercase_string)  # Output: "   HELLO, WORLD!   "

# Capitalize the string (first character uppercase, rest lowercase)
capitalized_string = sample_string.capitalize()
print("Capitalized:", capitalized_string)  # Output: "   hello, world!   "

# Check if the string starts with a specific prefix
starts_with_hello = sample_string.startswith("Hello")
print("Starts with 'Hello':", starts_with_hello)  # Output: False

# Check if the string ends with a specific suffix
ends_with_world = sample_string.endswith("World!")
print("Ends with 'World!':", ends_with_world)  # Output: True

# Find the index of the first occurrence of a substring
index_of_hello = sample_string.find("Hello")
print("Index of 'Hello':", index_of_hello)  # Output: 3

# Replace a substring with another substring
replaced_string = sample_string.replace("World", "Universe")
print("Replaced:", replaced_string)  # Output: "   Hello, Universe!   "

# Split the string into a list of substrings using a delimiter
split_string = sample_string.split(",")
print("Split:", split_string)  # Output: ['   Hello', ' World!   ']

# Join a list of substrings into a single string using a delimiter
joined_string = ", ".join(["apple", "banana", "cherry"])
print("Joined:", joined_string)  # Output: "apple, banana, cherry"

# Joining a list of strings with a comma as the delimiter
my_list = ["apple", "banana", "cherry"]
result = ", ".join(my_list)
print(result)

a='rohan'
n='rawat'
print(" ".join([a.capitalize(),n.capitalize()]))


print('*'*50)

# List Functions Example

# Define a sample list
sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Get the length of the list
list_length = len(sample_list)
print("Length:", list_length)  # Output: 11

# Find the maximum and minimum values in the list
max_value = max(sample_list)
min_value = min(sample_list)
print("Max Value:", max_value)  # Output: 9
print("Min Value:", min_value)  # Output: 1

# Count the number of occurrences of a specific element in the list
count_5 = sample_list.count(5)
print("Count of 5:", count_5)  # Output: 3

# Sort the list in ascending order (in-place)
sample_list.sort()
print("Sorted (Ascending):", sample_list)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# Sort the list in descending order (in-place)
sample_list.sort(reverse=True)
print("Sorted (Descending):", sample_list)  # Output: [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]

# Reverse the order of elements in the list (in-place)
sample_list.reverse()
print("Reversed:", sample_list)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# Create a shallow copy of the list
shallow_copy = sample_list.copy()
print("Shallow Copy:", shallow_copy)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# Append an element to the end of the list
sample_list.append(7)
print("Appended:", sample_list)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9, 7]

# Remove the first occurrence of a specific element from the list
sample_list.remove(3)
print("Removed:", sample_list)  # Output: [1, 1, 2, 3, 4, 5, 5, 5, 6, 9, 7]

# Insert an element at a specific index in the list
sample_list.insert(2, 8)
print("Inserted at Index 2:", sample_list)  # Output: [1, 1, 8, 2, 3, 4, 5, 5, 5, 6, 9, 7]

# Pop an element from the list at a specific index
popped_element = sample_list.pop(4)
print("Popped Element:", popped_element)  # Output: 3
print("List After Pop:", sample_list)  # Output: [1, 1, 8, 2, 4, 5, 5, 5, 6, 9, 7]

# Extend the list by adding elements from another iterable
sample_list.extend([0, 1, 2])
print("Extended:", sample_list)  # Output: [1, 1, 8, 2, 4, 5, 5, 5, 6, 9, 7, 0, 1, 2]

print(max(['rohan', 'rajveer'], key=len))

print(round(2.4567774,3))