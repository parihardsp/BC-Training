class all:
    def feature1(self):
        print('Feature 1 is working')

    def feature2(self):
        print('Feature 1 is working')


class B:
    def feature3(self):
        print('Feature 3 is working')

a1=all()

a1.feature1()
a1.feature2()

b1=B()
b1.feature3()

print('_'*50)
#Now class all is inherting all features of class B
print('Single level Inheritance:-')

class B(all):
    def feature3(self):
        print('Feature 3 is working')


#Here all is the SuperClass or ParentClass and B is the SubClass or Child Class
a2=B()

a2.feature1()
a2.feature3()

print('Multi level Inheritance:-')
class C(B):
    def feature10(self):
        print('This is feature 10 of Class C')
c1=C()
c1.feature1() #it can access features of parent class B as well as grandparent class A


print('Multiple Inheritance:- ')
class D:
    def feature20(self):
        print('This is feature 20 of Class D')

class C(all,D):
    def feature10(self):
        print('This is feature 10 of Class C')
# This will only access the features of CLass all and Class D

c2=C()
c2.feature20()
c2.feature1()

print("-"*100)

class A:
    def __init__(self):
        print("In A init")

    def feature1(self):
        print('Feature 1-A is working')

    def feature2(self):
        print('Feature 1 is working')


class B(A):
    def __init__(self):
        super().__init__()
        print("In B init")

    def feature1(self):
        print('Feature 1-B is working')

    def feature4(self):
        print('Feature 4 is working')

a1=B()
print("-"*50)
# So, if you create object of subclass, it will first try to find the __init__ of subclass, if not then, it will find it in superclass
# But if both have init and you want to call init of superclass also, so use super().__init__ in init constructor of subclass
class F:
    def __init__(self):
        print("In F init")

    def feature1(self):
        print('Feature 1-F is working')

class C(F,A):
    def __init__(self):
        super().__init__()
        print("In C init")

c1=C()

#In Multiple Inheritance we use MRO, Method Resolution Order,when we give super().__init()__ in the constructor, it will go from LEFT to RIGHT
c1.feature1() # so, class A and F has same method called feature1, but it will give you feature 1 from class A not F as we are going from left to right