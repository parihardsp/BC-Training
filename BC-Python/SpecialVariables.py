#__name__
"""
This special variable is used to determine whether a Python script is being run as the main program or if it's being imported as a module into another script.
When a Python script is run directly, __name__ is set to "__main__". When it's imported as a module, __name__ is set to the name of the module.
"""

import file_import # Now we cannot access the print of 'file_import' as we have use condition (if __name__ == "__main__":) there.

__name__='mainless'
print(__name__)  #we have changed the name of this file from __main__ to mainless

if __name__=='__main__':
    print('Hey')

class Martian:
    """ Someone who lives in Mars """

    def __init__(self,fn,ln):
        self.first_name=fn
        self.last_name=ln


m=Martian("Josko","Guardiol")

print(m.__doc__)
print(m.__dict__)

print('-'*100)
class Martian:
    """ Someone who lives in Mars """

    def __init__(self,fn,ln):
        self.first_name=fn
        self.last_name=ln

    def __setattr__(self, key, value):
        self.__dict__[key]=value

    def __str__(self):  #Used to define the human-redable string represenattion of object
        return f"{self.first_name} {self.last_name} "


m=Martian("Josko","Guardiol")
print(m.__str__())
print(m.__repr__())
print(id(m))



print('-'*100)

#Usally python default __setattr__ method stores each attributes in a special dict for us
#but now, i have defined the __setattr__ method in the class, so now python will not store it in the special dict(__dict__),
#we have to do it manually.

class Martian:
    """ Someone who lives in Mars """

    def __init__(self,fn,ln):
        self.first_name=fn
        self.last_name=ln

    def __setattr__(self, key, value):
        print(f">>>You set {key} = {value}")
        self.__dict__[key]=value

    def __getattr__(self,name):
        print(f">>>Get the  {name} attribute")

m=Martian("Josko","Guardiol")

#so, as we initialize the object, it will call the setattr method.
#But sill getattr is not called.

