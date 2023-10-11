'''
Class--> Design/Buleprint
Object--> Instance of a Class

Attributes --> Variables
Behavior --> Methods(Functions)

Argument (self) refers to the object itsel

'''

# class Computer:
#     def __init__(self):
#         print("in init")
#
#     def config(self):  #self is the object which we are passing
#         print(f"i5,16GB,1TB")
#
# a='8'
# comp1=Computer()
#
# print(type(8))      #in-built class / str class
# print(type(comp1))  #Custom-made class
#
# comp1=Computer()
# comp2=Computer()
#
# # Computer.config(comp1) #config method of class Computer is taking object comp1 as argument
# # Computer.config(comp2)
#
# comp1.config()
# comp2.config()


print('-' * 80)


class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(f"Config is {self.cpu}, {self.ram}")


comp1 = Computer('i5', '16 GB')
comp2 = Computer('Ryzen 7', '8 GB')

comp1.config()
comp2.config()

print('-' * 80)


class maths:
    def subtract(self, i, j):
        return i - j

    def add(self, i, j):
        return i + j


# constructing object-- objectName.methodName

# Calling function outside the class
m = maths()

print(m.subtract(10, 2))


# Calling function inside the class:
class maths1:
    def subtract(self, i, j):
        return i - j

    def add(self, i, j):
        return i + j

    def testsub(self):
        print(self.subtract(100, 4))


m = maths1()
m.testsub()

print('-' * 80)

# Attributes: class and instance attributes
# namespace is an area where you can create store obj/variables
''' we have  class namespace     --> Class & Static var are same
             instance namespace
'''


class Person:
    company = "Blenheim"  # class attribute / class variable

    def __init__(self):
        self.age = 90  # instance attribute/ instance variable, defined inside a class function/method


p1 = Person()
p2 = Person()

p1.age = 35  # change to instance attribute will only affect that particular instance/object

print(p1.age)
print(p2.age)

p1.company = 'Chalcot'  # Change to class attribute will affect all the instances, but here we are calling it from instance name.
print(p1.company)
print(p2.company)

Person.company = 'Chalcot'  # Change to class attribute will affect all the instances
print(p1.company)
print(p2.company)

#  When n instance of a class is created, the class constructor function is automatically called
# __init__ is the Constructor.
# It contains code for initializing a new instance of the class to a specific itital state


print('-' * 80)
'''
METHODS: Instance/Static/Class
'''


class Student:
    school = 'St Adams'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.marks3 = m3

    def avg(self):
        return round((self.m1 + self.m2 + self.marks3) / 3, 3)

    def get_m1(self):  # getters/ are accessors , we can only access the value
        return self.m1

    def set_m1(self, value):  # setters/ are mutators, we can change the value
        self.m1 = value


s1 = Student(50, 70, 98)
s2 = Student(90, 40, 33)

print(s1.avg())
print(s2.avg())


class Student:
    school = 'St Adams'
    place = 'Mumbai'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.marks3 = m3

    # instnace method
    def avg(self):
        return round((self.m1 + self.m2 + self.marks3) / 3, 3)

    # class method
    @classmethod  # you have to mention the decorators
    def getSchool(cls):
        return cls.school

    # static method #when you dont want to do anything with the class or instance variables/ something extra
    @staticmethod
    def info():
        print("This is Student Class...")


s1 = Student(50, 70, 98)
s2 = Student(90, 40, 33)

print(s1.avg())
print(s1.info())
print(Student.getSchool())
Student.info()

print("_" * 100)


'''
INNER CLASS
'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.lap=self.Laptop()    #Laptop('Goa')

    def show(self):
        print(self.name,self.age)
        self.lap.show()

    class Laptop:
        def __init__(self):
            #self.place=place
            self.brand='HP'
            self.cpu='Ryzen 7'
            self.ram='16 GB'

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = Student('Jenny',19)
s2 = Student('Sherya',21)

s2.show()

#s2.Laptop.brand='Lenevo' # cant change this as we are not taking any parameters in the Laptop class



