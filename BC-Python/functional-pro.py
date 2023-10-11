"""
Concepts of Functional Programming (F.P.) in Python:
Functions are 1st class citizen.
In F.P., we use immutable data structures. i.e. strings,tuples
In F.P., we us pure functions
F.P. relies on recursion
Built-In functions in python: Map,Filter,Reduce,Zip
Lambda Functions, anonymous func, used for one-time operations.
Closures: Functions that remembers their enclosing space, even if they are called from outside of that scope.

"""

# MAP: map(function, iterable)

numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x * x, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

print('-'*80)

#FILTER:   filter(function, iterable)

evens = filter(lambda x: x % 2 == 0, numbers)
even_list = list(evens)
print(even_list)


print('-'*80)

#REDUCE: functools.reduce(function, iterable[, initializer])
import functools

numbers = [1, 2, 3, 4, 5]
product = functools.reduce(lambda x, y: x * y, numbers,2)
#flow= 2*1=2, 2*2=4, 4*3=12, 12*4=48, 48*5=240

print(product)

print('-'*80)

#Zip: zip(iterable1, iterable2, ...)

names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]

# Using zip to combine names and scores
combined = zip(names, scores)
combined_list = list(combined)

print(combined_list)
# Output: [('Alice', 95), ('Bob', 87), ('Charlie', 92)]
