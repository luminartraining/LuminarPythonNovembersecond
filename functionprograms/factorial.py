#create a function to find factorial of a given number

def factorial(num):#num=5
    fact=1#fact=1
    for i in range(1,(num+1)):#(1,(1+5)) 1,2,3,4,5,6
        fact=fact*i#fact=1*1=1   ,1*2=2 , 2*3=6 , 6*4=24 24*5=120
    return fact #120


print(factorial((5)))#120