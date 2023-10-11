'''
#Encaptulation:
It is the property that restricts the ability to override the values for the objects within the setters
'''


class Person:
    __company = "Blenheim"

    def __init__(self, name, age, salary):
        self.__name = name
        self.age = age
        self.__salary=salary

    def salary_increment(self, pay_rate):
        self.__salary = self.__salary * pay_rate
        return self.__salary


    @property  # Decorater for making the class attribute fully private
    def company(self):
        return self.__company


    @company.setter  # Decorater for modifying  the class attribute
    def company(self, new_company):
        # You can add validation logic here if needed
        self.__company = new_company


# Example usage:
p = Person("John", 30,200)
print(p.company)  # Accessing the company attribute using the property
p.company = "Chalcot"  # Modifying the company attribute using the property
print(p.company)

print('-'*80)
#ABSTRACTION:
#It is the property of hiding unnecessary info from the instances
# So, in other programming lang. like Java we can use access modifiers like private & public to hide these stuffs(attributes/functions)
#But in python we do so by using double underscore(__) before the name of methods or attributes

class Email:
    def __init__(self,name,quantity):
        self.name=name
        self.quantity=quantity
    def __connect(self,smtp_server):
        return f"Connecting to SMTP server: {smtp_server}"
    def __body(self):
        return f"""
        Hello Someone
        The item: {self.name},Only {self.quantity} peices left now.
        Thanks & Regards
        Deepak
        """
    def __subject(self):
        return f"Regarding {self.name} Availability"
    def send_email(self):
        self.__connect("X-server")
        self.__subject()
        self.__body()

        return f"{self.__connect('X-server')} \n{self.__subject()} \n{self.__body()}"


e=Email('iPhones', 20)
print(e.send_email())

print('-'*80)

#POLYMORPHISM:
name="Jimmy"  #str
print(len(name))

some_list=['Jimmy','Dave']
print(len(some_list))
