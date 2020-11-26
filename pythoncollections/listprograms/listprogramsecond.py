#add a limit of numbers

limit=int(input("enter limit"))
lst=[]
for i in range(1,limit+1):
    lst.append(i)
print(lst)

even=[]
od=[]
for num in lst:
    if(num%2==0):
        even.append(num)
    else:
        od.append(num)
print(even)
print(od)
#store odd and even numbers in to seperate list