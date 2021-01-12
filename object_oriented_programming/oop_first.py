
class Person:
    company_name="luminar Technolab"

    @classmethod
    def print_company_name(cls):
        print(Person.company_name)
    @staticmethod
    def set():
        print("inside util function")



    def __init__(self,name1,age1,gender1):
        self.name = name1
        self.age = age1
        self.gender = gender1


    def print_person(self):
        print("name=",self.name)
        print("age=",self.age)
        print("gender=",self.gender)



obj=Person("ajay",25,"male")
obj.print_person()



#diffrenet type of variables are instance variables,static/class variables


#different types of method(self arg)
#acessing instance method reference.method



#1)instance method

#2)static method
#===>
Person.util()
Person.print_company_name()
#classlevel method
#creating object
# refenecename=ClassName()


#constructor()
#the duty of constructor is initializing instance variables

#constructor name always() __init__()
#constructor invoked  automaticallu at the time of object creation
# obj=Person()#created an object
# obj.set_person("ajay",25,"male")
# obj.print_person()
# obj1=Person()#created an object
#
# obj1.set_person("vijay",27,"male")
# obj1.print_person()
#
# obj1.age=28
#
# obj1.print_person()



