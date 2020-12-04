lst=[5,7,5,1,2,3,4]
#step1 we have to sort the array

lst.sort()
print(lst)
# 0   1   2    3   4  5   6
#[10, 20, 30, 40, 50, 60, 70]
# l       u     m
#step2


low=0
upp=len(lst)-1 #6

mid=(low+upp)//2  #0+7//2=3

element=40
#case1 if(element >lst[mid): 60>40:
#low=mid+1
#case 2 elif(element<lst[mid]):
#upp=mid-1
#case 3 if(element==lst[mid]) : prinrt element found




