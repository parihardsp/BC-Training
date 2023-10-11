a=100
def show():
    a=20
    b=27
    print(a)
show()
print(a)
#print(b) b is local var, so cant be accessed outside of that scope.

print('-'*50)

a=9
def show():
    global a #used to access the global_variable and also helps in modifying it.
    a=100
    b=200
    print(a)
show()
print(a)


print('-'*50)

def display():
    x=30
    def show():
        global x
        x=8
    print(f"Value of 'x' before calling show() is {a}")
    show()
    print(f"Value of 'x' after calling show() is {a}")

display()
print(x) #x=9 which is inside of a fun, which is inside of another fun display. but we have assigned it using global keyword
