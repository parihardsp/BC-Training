'''
DUCK TYPING
So, If there is a bird, that quacks like a duck, swims like a luck, walks like a duck, Then it is a duck
Similiarly, if we have class having a particular method to it
If there is any object IDE and has methode execute, then we can use it
'''

class PyCharm():
    def execute(self):
        print('Compling')
        print('Running')

class VSCode():
    def execute(self):
        print('Theams')
        print('Compling')
        print('Running')

class MyIDE():
    def execute(self):
        print('Spell Check')
        print('Convention Check')
        print('Compling')
        print('Running')

class Laptop:
    def code(self,ide):
        ide.execute()

ide=MyIDE()

lap1=Laptop()
lap1.code(ide)

print('-'*50)

a=5
b=6
print(a+b)
print(int.__add__(a,b))  #hold ctrl and click on method class(here, class int)
print(str.__add__('5','6'))

print('-'*50)
#Operator Overloading

class Student:
    def __init__(self,sci_marks,maths_marks):
        self.m1=sci_marks
        self.m2=maths_marks

    def gett(self):
        print(self.m1)

    def __add__(self, other):
        sci_marks=self.m1 + other.m1
        math_marks=self.m2 + other.m2
        s3=Student(sci_marks,math_marks)
        return s3

    def __gt__(self, other):
        r1=self.m1+self.m2
        r2=other.m2+other.m1
        if r1>r2:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.m1},{self.m2}"

s1=Student(50,60)
s2=Student(38,55)


s1.gett()
s3=s1+s2  #--> Student.__add__(s1,s2)
print(s3.m2)

if s1>s2:
    print('s1 obj wins')
else:
    print('s2 obj wins')

a=8
print(a)  #printing value of a
print(a.__str__())
print(s1)

print('-'*50)


"""
TYPES OF POLYMORPHISM: Method Overloading, Method Overriding (not in python)
When we have two methods with the same name, but with different parameters , it is called method overloading
When we have two methods with the same name, & same no of parameters , it is called method overriding
"""

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,a=None,b=None,c=None): #or sum(self,*args)
        s=0

        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s

s1=Student(40,50)

print(s1.sum())


#method overriding example

class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):
        print("in B show")

a1=B()
a1.show()  # so, the show() in B class overrides the show() of parent class A


