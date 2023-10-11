"""
Iterables:
An iterable is any Python object capable of returning its elements one at a time.
It provides a way to loop over its elements, typically using a for loop or a comprehension. Common iterable objects in Python include lists, tuples, strings, dictionaries, and sets. To check if an object is iterable,
you can use the iter() function and see if it raises a TypeError:
"""

nums =[10,20,30,40]

# for num in nums:
#     print(num)

print(dir(nums))  #__iter__ method is present

try:
    iterator = iter(nums)       #making nums list as iterator.
    print("This object is iterable.")
except TypeError:
    print("This object is not iterable.")

print(iterator.__next__())
print(next(iterator))

#Iterator is an object with a state, so that it remembers where it is, during iteration.
# When again you call next, it knows the previous value .

print('-'*80)
"""
Iterator:
An iterator is an object that implements two special methods: __iter__() and __next__(). 
Iterators are used to iterate over elements in an iterable sequentially, one at a time. The __iter__() method returns the iterator object itself, and the __next__() method returns the next element in the iteration.
Here's a simple example of a custom iterator for counting from 0 to a specified limit:
"""



class Counter:
    def __init__(self, limit=10):
        self.limit = limit
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.value < self.limit:
            result = self.value
            self.value += 1
            return result
        else:
            raise StopIteration

# Using the custom iterator
counter = Counter()        #this is iterator as well as iteratable
for num in counter:
    print(num)
