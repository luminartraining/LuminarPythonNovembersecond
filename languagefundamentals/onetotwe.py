#print 1 to 12

#1 2 3 4
#5 6 7 8
#9 10 11 12

cnt=0
for i in range(1,13):
    print(i,end="\t")
    cnt += 1
    # if cnt==4:
    #     print()
    #     cnt=0
    if i%4==0:
        print()


