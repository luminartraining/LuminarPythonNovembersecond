class Employee:
    def __init__(self,id,name,exp,salary,desig):
        self.id=id
        self.name=name
        self.exp=exp
        self.salary=salary
        self.desig=desig
    def __str__(self):
        return self.name+" "+self.id

f=open("employee","r")
lst=[]
for lines in f:
    id, name, exp, salary, desig=lines.rstrip("\n").split(",")

    ob=Employee(id,name,exp,salary,desig)
    lst.append(ob)


for emp in lst:
    print(emp)
#print all employee name in uppercase

ename=list(map(lambda emp:emp.name.upper(),lst))
print(ename)

#print employee details whose designation="developer

devops=list(filter(lambda emp:emp.desig=="developer",lst))
for emp in devops:
    print(emp)

#print employee details whose salary >23000

highsal=list(filter(lambda emp:int(emp.salary)>23000,lst))
for emp in highsal:
    print(emp.name,",",emp.desig,",",emp.salary)

#lambda
#map()
#filter()

