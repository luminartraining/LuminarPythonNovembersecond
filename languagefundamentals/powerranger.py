#2

#2+22=24

#3 3+33+333=369

#4 4+44+444+4444


number=input("enter number")#"3"

i=1
total=0
while(i<=int(number)):#1<=3 2<=3 3<=3
    # print(number*i)#"3"*1="3"  "3"*2=33 "3"*3="333"
    data=number*i
    total=total+int(data)
    i+=1#i=2 3
print(total)
