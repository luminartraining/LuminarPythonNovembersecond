#123 ->321

num=int(input("enter num"))#123
res=0
while(num!=0):#123!=0 12!=0 1!=0 0!=0
    digit=num%10#123%10=3 12%10=2 1%10=1
    res=res*10+digit# 0*10+3=3 3*10+2=32 32*10+1=321
    num=num//10 #123//10=12 12//10=1 1//10=0

print(res)#321

#multiplication table
#123 1**3+2**3+3**3=1+8+27=36