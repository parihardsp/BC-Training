def name(a):
    return f"Hello,{a}"


def factorial(x):
    print(x)
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)
print(factorial(5))

def fibo(n):
    a = 0
    b = 1
    ls=[0,1]
    for i in range(n-2):
        c=a+b
        a=b
        b=c
        ls.append(c)
    return ls

print(fibo(10))



print(name('Deepak') * 3)


def greet(a, b):
    return f"Hi {a} \nYour age is {b}"


def summ(*a):
    total = 0
    for i in a:
        total = total + i
    return total


print(summ(5, 2, 4, 100))
print(greet(10, 'Deepak'))
print(greet(b=10, a='Deepak'))


# CONVENTION- Normal Arguments --> Arbitary Positional Agruments --> Arbitary Keywords Agruments
# *args are passed in form of TUPLE
# **kwargs are passed in form of dictonary

def multiply(*args):
    total = 1
    for i in args:
        total *= i
    return total, args[-1]


print(multiply(10, 2, 4, 6))


def length(x):
    count = 0
    for i in x:
        count += 1
    return count


a = [1, 2, 2, 3, 4, 5]
print(a[:10])
print(length(a))
print(a[:(length(a) - 1)])

print('-' * 20)

import statistics

def stat(lst):
    return statistics.mean(lst), statistics.median(lst), statistics.mode(lst)

mean,mode,median=stat([10,5,90,70,100,95,90,9,8])
print(mode)
print(median)
print(mean)


