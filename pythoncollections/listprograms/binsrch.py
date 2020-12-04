lst=[21,20,18,22,7,2,25]
lst.sort()
print(lst)
# l             l    m    u
#[2, 7, 18, 20, 21, 22, 25]
# 0  1   2   3   4   5   6
low=0
upp=len(lst)-1#6
flg=0
element=int(input("enter element you want to search"))#22
while(low<=upp):#0<=6 4<=6
    mid=(low+upp)//2  #0+6//2=3 # 4+6/2=10/2=5
    #case1
    if(element>lst[mid]):#22>22
        low=mid+1#low=3+1=4
    elif(element<lst[mid]):#22<22
        upp=mid-1
    elif element==lst[mid]:#22==22
        flg+=1
        break
if flg==0:
    print("no element")
else:
    print("element found")