lst=[10,11,12,13,14,15]

# res=list(map(lambda num:num**2,lst))
# print(res)

even=list(filter(lambda no:no%2==0,lst))
print(even)


emplyees=["ajay","vijay","anil","danie","tom","joy"]

#convert all employeenames to uppercase
enames=list(map(lambda name:name.upper(),emplyees))
print(enames)


#print all emplyee name starting with a
enamea=list(filter(lambda name:name[0]=='a',emplyees))
print(enamea)
