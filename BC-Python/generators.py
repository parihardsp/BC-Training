def count_up_to(start,limit):
    while start <= limit:
        yield start
        start += 1

# Using the generator
for num in count_up_to(1,5):
    print(num)

print()


# Using return in a regular function
def return_example():
    for i in range(3):
        return i

result = return_example()
print("The Return Keyword")  #Do not remember the state of the function
print(result)  # Output: 0
print(result)
print(result)

# Using yield in a generator function
def yield_example():
    for i in range(3):
        yield i

gen = yield_example()
print("The Yeild Keyword")  #Does remember the state of the function
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
