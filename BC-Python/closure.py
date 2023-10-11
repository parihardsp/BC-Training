#Closures

# def outer_func():
#     msg='Hello'
#     def inner_func():
#         print(msg)
#     return inner_func()
#
# outer_func()

#Now returning inner_func without excueting it.
def outer_func():
    msg='Hello'
    def inner_func():
        print(msg)
    return inner_func

my_func= outer_func()
#now the variable my_func is equal to the inner func as it was returned

print(f'my_func variable name is now : {my_func.__name__}')

#Now even though we are done with the execution of outer_func in linw 18,
# but still the inner func access to that msg variable.

my_func()

print('-'*100)


def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_5 = outer_function(5)  # Closure created with x = 5

result1 = add_5(3)  # Output: 5 + 3 = 8
result2 = add_5(7)  # Output: 5 + 7 = 12

print(result1)
print(result2)
