class Parent:
    def m1(self):
        print("inside parent")


class Child(Parent):
    def m2(self):
        print("inside Child")


class SubChild(Child):
    def m3(self):
        print("inside subchild")
sc=SubChild()
sc.m3()
sc.m2()
sc.m1()

ch=Child()
# ch.m3()error
ch.m2()
ch.m1()


pt=Parent()
pt.m1()