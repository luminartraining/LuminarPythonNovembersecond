#7 (2,3,4,5,6,)



number=int(input("enter number"))#4
if(number==2):
    print("prime number")
else:

    flg=0
    for i in range(2,number):#(2,3)
        if(number%i==0):#4%2==0
            flg+=1#flag=1
            break
    if(flg==0):
        print("prime number")
    else:
        print("not a prime number")

#read lowlimit and upplimit 10,50 print all primenumbers b/w 10-50

