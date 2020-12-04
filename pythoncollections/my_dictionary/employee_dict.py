employee={"eid":1000,"desig":"developer","exp":1,"company_name":"luminar"}



#print company name

print(employee["company_name"])

#chking for salary key is there
print("salary" in employee)

#add anew key value pair salary :30000
employee["salary"]=30000
print(employee)

#add 5000 more rs to current salary
employee["salary"]+=5000
print(employee)


# for key in employee:
#     print(key,",",employee[key])#{'eid': 1000, 'desig': 'developer', 'exp': 1, 'company_name': 'luminar', 'salary': 30000}
#     #eid

for k,v in employee.items():
    print(k,v)
