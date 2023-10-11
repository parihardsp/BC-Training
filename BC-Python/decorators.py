#DECORATORS:

def decorator_func(og_func):
    def wrapper_func():
        print('Welcome to Switz')
        return og_func()
    return wrapper_func

@decorator_func
def show():
    print('Deepak')

show()
# show=decorator_func(show)  #Alternative method
# show

print('-'*50)

class deco_class:
    def __init__(self,og_func):
        self.og_func=og_func
    def __call__(self, *args, **kwargs):
        print('Welcome to Switz, in the class')
        return self.og_func()

@deco_class
def show():
    print('Deepak Parihar')

show()

print('-'*50)

#For logging purpose

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling '{func.__name__}' function, with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' returned {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

add(5,10)

print('-'*50)
#For Authentication:
#
# def requires_authentication(func):
#     def wrapper(*args, **kwargs):
#         if is_authenticated():
#             return func(*args, **kwargs)
#         else:
#             raise PermissionError("Authentication required")
#     return wrapper
#
# @requires_authentication
# def secure_function():
#     return "This function requires authentication"
#
# secure_function()

print('-'*50)
#For performance measurement:

import time

import time

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute")
        return result
    return wrapper

@measure_execution_time
def time_consuming_function():
    # Simulate a time-consuming task (e.g., calculating a large sum)
    result = 0
    for i in range(1000000):
        result += i
    return result

# Call the decorated function
result = time_consuming_function()
print(f"Result: {result}")


print('-' * 50)
#Route Handling in Web Framework:

# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return "Hello, World!"
