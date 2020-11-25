num1=int(input("enter value for num1"))#50
num2=int(input("enter value for num2"))#42
num3=int(input("enter value for num3"))#45
if((num1>num2)&(num1>num3)):# 50> 45 & 50>40 firtst=50
    #num2or num3
    if(num2>num3): #42>45
        print(num1,",",num2,",",num3)
    else:#second=45
        print(num1,",",num3,",",num2)

elif((num2>num1)&(num2>num3)):
    #num2
    if (num1 > num3):
        print(num2,",",num1,",",num3)
    else:
        print(num2,",",num3,",",num1)

elif((num3>num1)&(num3>num2)):
    #num3
    if (num1 > num2):
        print(num3,",",num1,",",num2)
    else:
        print(num3,",",num2,",",num1)

