def space():
    print("-" * 40)

#LISTS

ls=['Rohan','Bajaj',1,25,32,'Sachin'] #it cannot be sorted as it has different data types in it.
lst=['Rohan','Shyam','Gulab','Jasmaine','Robert']
lst.sort()
print(lst)

# Creating a list
my_list = [1, 2, 3, 4, 5]

# Append: Adds an element to the end of the list
my_list.append(6)  # my_list is now [1, 2, 3, 4, 5, 6]

# Insert: Inserts an element at a specific position
my_list.insert(2, 7)  # my_list is now [1, 2, 7, 3, 4, 5, 6]

# Remove: Removes the first occurrence of a value
my_list.remove(3)  # my_list is now [1, 2, 7, 4, 5, 6]

# Pop: Removes and returns the last element
popped_element = my_list.pop()  # popped_element is 6, my_list is [1, 2, 7, 4, 5]

# Extend: Appends elements of another list to the current list
other_list = [8, 9]
my_list.extend(other_list)  # my_list is now [1, 2, 7, 4, 5, 8, 9]

# Count: Returns the number of occurrences of an element
count_4 = my_list.count(4)  # count_4 is 1

# Sort: Sorts the list in ascending order
my_list.sort()  # my_list is now [1, 2, 4, 5, 7, 8, 9]

# Reverse: Reverses the order of elements in the list
my_list.reverse()  # my_list is now [9, 8, 7, 5, 4, 2, 1]

# Indexing and Slicing
first_element = my_list[0]  # first_element is 9
sliced_list = my_list[2:5]  # sliced_list is [7, 5, 4]

# List Comprehension: Creating a new list based on an existing list
squared_list = [x**2 for x in my_list]  # squared_list is [81, 64, 49, 25, 16, 4, 1]

# Printing the final list
print("Final List:", my_list)

space()

#TUPLES

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5, 4)

# Indexing and Slicing
third_element = my_tuple[2]  # third_element is 3
sliced_tuple = my_tuple[1:4]  # sliced_tuple is (2, 3, 4)

# Count: Returns the number of occurrences of a value
count_4 = my_tuple.count(4)  # count_4 is 2

# Index: Returns the index of the first occurrence of a value
index_3 = my_tuple.index(3)  # index_3 is 2

print('my_tuple: ',my_tuple)

space()

#SETS

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Add: Adds an element to the set
my_set.add(6)  # my_set is now {1, 2, 3, 4, 5, 6}

# Remove: Removes an element from the set
my_set.remove(3)  # my_set is now {1, 2, 4, 5, 6}

# Discard: Removes an element from the set (no error if not found)
my_set.discard(7)  # my_set remains the same

other_set = {5, 6, 7}
print('my_set',my_set)
print('other_set',other_set)
# Union: Returns the union of two sets

union_result = my_set.union(other_set)  # union_result is {1, 2, 4, 5, 6, 7}
print('union_result: ',union_result)

# Intersection: Returns the intersection of two sets, common elements b/w both the sets
intersection_result = my_set.intersection(other_set)  # intersection_result is {5, 6}
print('intersection_result: ',intersection_result)

# Difference: Returns the difference between two sets, elements which are only in first set
difference_result = my_set.difference(other_set)  # difference_result is {1, 2, 4}
print('difference_result: ',difference_result)

# Symmetric Difference: Returns the symmetric difference between two sets, all the other elements in both the sets apart from common elements (union - intersection)
symmetric_difference_result = my_set.symmetric_difference(other_set)  # symmetric_difference_result is {1, 2, 4, 7}
print('symmetric_difference_result: ',symmetric_difference_result)

space()

# Creating a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Accessing values by keys
name_value = my_dict['name']  # name_value is 'Alice'

# Get: Returns the value associated with a key (with a default value)
age_value = my_dict.get('age', 25)  # age_value is 30
country_value = my_dict.get('country', 'USA')  # country_value is 'USA'

# Keys: Returns a list of keys
keys_list = list(my_dict.keys())  # keys_list is ['name', 'age', 'city']

# Values: Returns a list of values
values_list = list(my_dict.values())  # values_list is ['Alice', 30, 'New York']

# Items: Returns a list of key-value pairs
items_list = list(my_dict.items())  # items_list is [('name', 'Alice'), ('age', 30), ('city', 'New York')]

update_dict=my_dict.update({'country': 'USA'}) #if this key already exist it will just update the value.

pop_dict=my_dict.pop('age')

print(my_dict)
print(my_dict.items())
print(type(my_dict.keys()))
print(list(my_dict.keys()))

print(my_dict.get('age'))  #wont show error just returns None
print(type(my_dict.get('age')))

space()
#COMPREHENSIONS

squares = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]
squares_dict = {x: x**2 for x in range(1, 6)}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

if_comprehensions=[x for x in range(10) if x%2 == 0 if x<7]
ifelse_comprehensions=[ x if x%3==0 else 'ok' for x in range(8)]
print(squares)
print(squares_dict)
print(if_comprehensions)
print(ifelse_comprehensions)


space()
ifelse_compre=['*'*i if i else '*' for i in range(6)]
ifelse1_compre=['*'*(i+1) for i in range(6)]
print(ifelse_compre)
print(ifelse1_compre)

space()
#SHALLOW & DEEP COPY
import copy

original_list = [1, [2, 3]]
shallow_copied_list = original_list.copy()
deep_copied_list = copy.deepcopy(original_list)

original_list[1][0] = 4  # Modify a nested element
shallow_copied_list[1].append(5)

print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)  # Shallow copy reflects the change
print("Deep Copied List:", deep_copied_list)  # Deep copy remains unaffected
