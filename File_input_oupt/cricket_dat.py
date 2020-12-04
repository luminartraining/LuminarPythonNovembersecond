f=open("data","r")
dict={}
for lines in f:
    #Zampa comes back on.\n
    words=lines.rstrip(".\n").split(" ") #Zampa comes back on.\n
    print(words)
    #['Zampa', 'comes', 'back', 'on']
    for word in words:
        if (word not in dict):
            dict[word]=1
        else:
            dict[word]+=1
print(dict)

#find highest frequency word
#mtehod 1
# lst=[]
# for k,v in dict.items():
#     lst.append(v)
# high=max(lst)
#
# for k,v in dict.items():
#     if(v==high):
#         print(k,v)

#method 2
# high=max(dict,key=dict.get)
# print(high)
