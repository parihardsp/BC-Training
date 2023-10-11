"""
Exception Handling:
Try-Except Block:
Try Block: Write the code you want to test
Except Block: Errors which you are exception, for default: except Exception as e
            You can use more than one except block, i.e ValueError, IndexError etc

"""
a=input("Enter the number ")
print(f"Multiplication table of {a} is:")

try:
    for i in range(1,5):
        print(f"{int(a)*i}")

except Exception as e:
    print(f"Error : {e}")

print('Code is completed')



print('-'*80)
try:
    # Code that may raise an exception
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2

except ZeroDivisionError as e:
    # Handle division by zero exception
    print("Error, ZeroDiv:", e)

except ValueError as e:
    # Handle invalid input (non-integer) exception
    print("Error, ValueError:", e)

else:
    # Code to execute if no exceptions are raised10
    print("Result:", result)

finally:
    # Cleanup or resource release code (always executed)
    print("Execution complete.")

print('-'*80)

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print("Error:", e)

print('-'*80)

class MyCustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

def my_function(x):
    if x < 0:
        raise MyCustomError("Input must be non-negative.")
    return x

try:
    result = my_function(-5)
except MyCustomError as e:
    print("Error:", e)

# Output: Error: Input must be non-negative.

