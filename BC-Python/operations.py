import Loops
# Arithmetic Operations
num1 = 10
num2 = 4

# Addition
result_addition = num1 + num2  # result_addition will be 14

# Subtraction
result_subtraction = num1 - num2  # result_subtraction will be 6

# Multiplication
result_multiplication = num1 * num2  # result_multiplication will be 40

# Division
result_division = num1 / num2  # result_division will be 2.5

# Floor Division- returns iteger part of the quotient
result_floor_division = num1 // num2  # result_floor_division will be 2

# Modulus
result_modulus = num1 % num2  # result_modulus will be 2

print("Addition:", result_addition)
print("Subtraction:", result_subtraction)
print("Multiplication:", result_multiplication)
print("Division:", result_division)
print("Floor Division:", result_floor_division)
print("Modulus:", result_modulus)

Loops.space()
# Ceiling Function
result_ceil = -(-4.3 // 1)  # result_ceil will be 5

# Floor Function
result_floor = 4.9 // 1  # result_floor will be 4

# Absolute Value
result_fabs = abs(-3.5)  # result_fabs will be 3.5

# Exponentiation
result_pow = 2 ** 3  # result_pow will be 8

# Square Root
result_sqrt = 25 ** 0.5  # result_sqrt will be 5.0

print("Ceil:", result_ceil)
print("Floor:", result_floor)
print("Absolute Value:", result_fabs)
print("Exponentiation:", result_pow)
print("Square Root:", result_sqrt)

Loops.space()

import math

print(math.ceil(4.5))            # -(-4.5 // 1)
print(math.floor(4.5))           #  (4.5 // 1)

print(math.ceil(-2.5))
print(math.floor(-2.5))


a=5
b=5
print(id(a))
print(id(b))
print(a==b)  # equality operator compares the value of the object(variable)
print(a is b) #identity operator is comparing the memory address of the object, here a,b are pointing to same address having value '5'

name='Rohan Rawat'
print('han' in name)
print( 'RR' in name)