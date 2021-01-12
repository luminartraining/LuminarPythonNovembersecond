#method overriding


class Pesron:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print_person(self):
        print("name=",self.name,"\t","age=",self.age)
    def __str__(self):
     return self.name

obj=Pesron("ajay",25)
obj.print_person()

print(obj)#__str__

#__main__ .ClassName object at hexadecimal value
 #<__main__.Pesron object at 0x7f407d39c978>
#classname
#ajay 25
#