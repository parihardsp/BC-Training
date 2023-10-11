"""
First-Class Functions:
In Python, functions are considered first-class citizens, which means they can be treated like any other data type, such as integers, strings, or lists. This allows you to:

Assign functions to variables.
Pass functions as arguments to other functions.
Return functions from other functions.
"""



# Assigning a function to a variable
def greet(name):
    return f"Hello, {name}!"

say_hello = greet
print(say_hello("Alice"))  # Output: Hello, Alice!

# Passing a function as an argument
def apply(func, arg):
    return func(arg)

result = apply(greet, "Bob")
print(result)  # Output: Hello, Bob!

# Returning a function from a function
def get_greeter():
    def greeter(name):
        return f"Hi, {name}!"
    return greeter

my_greeter = get_greeter()
print(my_greeter("Charlie"))  # Output: Hi, Charlie!
