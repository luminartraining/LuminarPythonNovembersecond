# for row in range(1,4):#row=1 row=2 row=3 row=4
#     for col in range(1,4):#col=1,2,3 4
#         print(col,end="\t")#
#     print()


#1  2   3
#1  2   3
#1  2   3
#

#*
#**
#***
#****
#
# for row in range(1,5):
#     for col in range(1,(row+1)):
#         print(col,end="\t")
#     print()



#1
#22
#333
#4444

#1
#12
#123
#1234






for row in range(1,5):
    for col in range(1,8):
        if row==4 or row+col==5 or col-row==3:
            print("*",end="")
        else:
            print(end=" ") 
    print()