# lst=[-2,-1,0,1,2,3,4]#find least +ve missing in
#
#
# # print(1 in lst)#chk for 1 is in list or not
#
# cnt=1
# for i in range(0,len(lst)):
#     if cnt in lst:#1 in lst 2 in lst 3 4 5
#         cnt+=1#cnt=2,3
#     else:
#         print(cnt ,"is missing least +ve missing integer")
#         break
#
# st={1,2,3,3,4}
# lst=list(st)
# print(lst[3])





lst=[-1,-2,0,1,2,3,4]

cnt=1
for num in lst:#num=-1,-2,0,1,2
    if(num>0):
        if(num==cnt):#1==1
            print("hello")
            cnt=cnt+1#cnt=2,35
            print(cnt)
        else:
            print(cnt,"is missing integer")
            break
