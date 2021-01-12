class Parent:
    def m1(self):
        print("inside parent")


class Child:
    def m1(self):

        print("inside Child")


class SubChild(Parent,Child):
    def m3(self):
        print("inside subchild")


sc=SubChild()
sc.m3()
sc.m1()

#instance variable
#static variable
#different type of method
#constructor
#inheritance(1,2,3)


