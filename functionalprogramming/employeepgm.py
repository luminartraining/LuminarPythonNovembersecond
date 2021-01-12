#find highest salary
from functools import *
class Employee:

    def __init__(self,eid,ename,desig,sal,exp):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.sal=sal
        self.exp=exp


    def __str__(self):

        return self.ename+","+self.desig


#read from file
f=open("employee","r")
employees=[]

for lines in f:
    eid,ename,desig,sal,exp=lines.rstrip("\n").split(",")
    employees.append(Employee(eid,ename,desig,sal,exp))

#highest salary

# highestsalary=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,
#                      list(map(lambda emp:emp.sal,employees)))
# print(type(highestsalary))
#print highset salaried employee details
# employee=list(filter(lambda emp:emp.sal==highestsalary,employees))
# for emp in employee:
#     print(emp.ename)
#



#find highest salary whose designation =developer



# developers=list(filter(lambda emp:emp.desig=="developer",employees))
#
#
# devsalary=list(map(lambda emp:emp.sal,developers))
#
#
# devehighest=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,devsalary)
#
# print(devehighest)



developer_highest=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,
                         list(map(lambda emp:emp.sal,
                                  list(filter(lambda emp:emp.desig=='developer',employees)))))
print(developer_highest)



