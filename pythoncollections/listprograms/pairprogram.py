lst=[1,2,3,4,6]
# 1 2 3 4 6
#   l   u
low=0
upp=len(lst)-1

element=7
pairs=[]
while(low<upp):
    total=lst[low]+lst[upp]
    if(element<total):
        upp=upp-1
    elif(element>total):
        low=low+1
    elif(element==total):
        print(lst[low],",",lst[upp])

        break
#total=lst[low]+lst[upp] 6+1 =7 1+4=5 2+4=6
#case 1 if(element < total) :6 <7 : moving upper bacwards upp=upp-1 6<5 6<6

#case2 elif(element>total):moving lower forward low=low+1 6>5 6>6


#case3 elif(total==elemet) 6==6

