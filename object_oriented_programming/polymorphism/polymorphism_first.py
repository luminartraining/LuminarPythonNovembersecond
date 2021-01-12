#polymorphism(many forms)
    #method overloading
    #method overriding
    #operator overloading


#m3thod overloading
#same method name but different number of parameters


# def add():
#     num1=10
#     num2=20
#     print(num1+num2)
#
# def add(num1,num2):#num1 ,num2 parameters
#     print(num1+num2)


class Meth:
    def add(self):
        print("inside no arg method")
    def add(self,no1):
        print("inside single arg method")
    def add(self,no1,no2):
        print("inside two arg method")

m=Meth()
m.add(10,20)
m.add(10)
#method overloading
#method overriding
#operator overloading

