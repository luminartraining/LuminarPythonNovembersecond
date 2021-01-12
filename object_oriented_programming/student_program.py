class Student:
    def set_student(self,rol,crse,total):
        self.rol=rol
        self.course=crse
        self.total=total
    def print_student(self):
        print("rollnumber=",self.rol)
        print("course",self.course)
        print("total=",self.total)


obj=Student()
obj.set_student(100,"mca",150)
obj.print_student()

obj.total+=15
print(obj.total)

