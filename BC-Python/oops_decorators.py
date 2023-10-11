#Property Decorator -- Read-Only attribute
class Person:
    __company = "Blenheim"    #this will only hide from getting accessed from outside the class, we can still modify it.

    def __init__(self,name,age):
        self.__name=name  #now using 2 '__' before attribute name will not allow the user to access this from outside the class
        self.age =age

    @property   # Decorater for making the class attribute fully private
    def name(self):
        return self.__name

    @name.setter     #This decorator is used to set the value of an attribulte even though it is private or Read-only attribute
    def name(self,value):
        if len(value) >10:
            raise Exception('Name is too long')
        self.__name=value


p1 = Person('Deepak',20)
p1.name='Ronit'   #Cannot change the attribute, due to @name.setter decorator

print(p1.name)

Person.company='Chalcot'
print(Person.company)
