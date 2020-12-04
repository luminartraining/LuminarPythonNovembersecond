students=[

    [100,"arun","bca",145],
    [101,"arjun","bca",125],
    [102,"varun","mca",160],
    [103, "tinu","mca",140],
    [104, "jeena","bcom",120],


]
import functools
tt=functools.reduce(lambda a,b:a if a>b else b,map(lambda obj:obj[3],students))
print(tt)
#print student names
for student in students:
    # [100,"arun","bca",145],
    print(student[1])
#print total of all student
total=0
for student in students:
    total=total+student[3]
print(total)
#list the details of student whose course=mca
for student in students:
    if student[2]=='mca':
        print(student)
#mca ? bca ?  bcom ?
mtotal=btotal=bctotal=0

for student in students:
    if student[2]=='mca':
        mtotal+=1
    elif student[2]=='bcom':
        bctotal+=1
    elif student[2]=='bca':
        btotal+=1
print("number of students in mca",mtotal)
print("number of in bca",btotal)
print(" bcom",bctotal)

#