#create a function print_employee_data()
#if we pass id pass argument that function will print employee name
#if we pass id and property =desig it will will print employee name and designation of that employee
#
# print_employee_date(id=1000)#ajay
# print_employee_data(id=1000,property="desig") ajay and 2

#step1 prcess the file and store it into dictionary

employee={}
f=open("employee","r")
for lines in f:
    #1000,ajay,developer,2,25000\n

    id,name,desig,exp,salary=lines.rstrip("\n").split(",")
    #id=1000,name=ajay,desig=developer,exp=2,salary=25000
    # #{
    #     "1000":{"id":1000,"name":"ajay","desig":"developer","exp":2,"salary":25000},
    #     "1001": {"id": 1001, "name": "vjay", "desig": "developer", "exp": 1, "salary": 15000},
    #     "1002": {"id": 1002, "name": "ajay", "desig": "developer", "exp": 2, "salary": 25000},
    #
    # #}
    employee[id]={"id":id,"name":name,"exp":exp,"salary":salary}


for k,v in employee.items():
    print(k,v)



def print_employee_data(**kwargs):
    print(kwargs)
    if "id" in kwargs:
        id=kwargs["id"]
        print(employee[id]["name"])

print_employee_data(id="1000")





#create function
