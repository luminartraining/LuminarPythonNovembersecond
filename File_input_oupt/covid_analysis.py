f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    words=lines.rstrip("\n").split(",")
    state=words[3].rstrip("***")
    cofirmed_cases=int(words[8])
    if(state not in dict):
        dict[state]=cofirmed_cases
    else:
        dict[state]=cofirmed_cases
lst=[]
for k,v in dict.items():
    #kerala,57256
    #(57256,kerala)
    lst.append([k,v])
# print(sorted(lst,reverse=True))
#
# high=max(dict,key=dict.get)
# print(high,dict[high])
print()
dict=sorted(dict,key=dict.get,reverse=True)
print(dict)
# students=[100,150]
# class Students:
#     def __init__(self,rol,mark):
#         self.rol=rol
#         self.mark=mark
# lst=[]
# ob=Students(100,150)
# lst.append(ob)
# ob1=Students(101,170)
