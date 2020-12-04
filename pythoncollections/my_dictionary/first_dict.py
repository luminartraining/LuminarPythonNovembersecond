#values stored in key:value pairs


students={'rolno':100,"name":"ajay","course":"mca","total":100}

#updating total with value 150
students["total"]+=50
print(students)

#chking for a key in dict
print("gender" in students)
print("name" in students)


#adding a new key value pairs
students["gender"]="male"
print(students)



#adding new key value pairs
#
#dictionary keys rolno,name,course
#we can acess the values only by using corressponding key
#name
print(students["name"])#ajay
#course
print(students["course"])
#duplicate keys are not allowed ,dupliacte value are allowede
print(students)


