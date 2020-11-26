lst=[5,4,3,2]#[9,10,11,12]
#lst=[5,6,3,4] [13,12,15,14]

total=sum(lst)#14
out=[]
for num in lst:#5
    out.append((total-num))
print(out)
