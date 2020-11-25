#read a number=2
#nmimum=8
#nmaximum=40

#3,4,5,6



#
# q4)given three input n,minimum&maximum find the number of values raised to the nth power that lie in the range[minimum,maximum]
# 	sample inp : n=2 minimum=49 maximum=65
#
# 	ouput: 49(7^2) and 64 (8^2)
#
#
# 	sample inp:n=3 minimum=1 maximum=27
# 	output:1(1^3),8(2^3),27(3^3)

n=int(input("enter number"))#3
min=int(input("enter minimum"))#1
max=int(input("enter max"))#27

for i in range(1,(max+1)):#1 to 27
    if i**n in range(min,(max+1)):#
        print(i,",",i,"^",n,"=",i**n)


