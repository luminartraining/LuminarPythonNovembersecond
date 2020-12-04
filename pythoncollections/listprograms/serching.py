#hackerrank
#account

lst=[1,2,3,4,5,6,7,8]

element=int(input("enter element"))

sorted()
#
# if(element in lst):
#     print("element found")
# else:
#     print("element not found")


flg=0
for num in lst:
    if(element==num):
        flg+=1
        break
    else:
        flg=0
if(flg==0):
    print("element not found")
else:
    print("element found")

lst=[1,2,3,4]
print(lst[2])
#linear serach,binary search,stack,queue
#data structures
 #1)linear structure-> arrays,stack,queue
#2)non linear-> trees,graph,linkedlist

#linked list
#  node[data,next]   [arjun,10234] [bibin,102345]
