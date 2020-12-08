
f=open("students","r")
students={}
for lines in f:
    #100,test,bca,140
    #rstrip,split by ,
    rol,name,course,total=lines.rstrip("\n").split(",")
    if rol not in students:
        students[rol]={"rol":rol,"name":name,"course":course,"total":total}
    else:
        pass
print(students)


def print_student(**kwargs):
    #kwargs={id:500,property:course}
    rol=kwargs["id"]
    if(rol in students):
        print(students[rol]['name'])
        if "property" in kwargs:
            prop=kwargs["property"]
            if(prop in students[rol]):
                print(students[rol][prop])
            else:
                print("invalid property")
    else:
        print('student doesnot exist')

id=int(input("enter id"))

property=input("enter property")
print_student(id=id)
