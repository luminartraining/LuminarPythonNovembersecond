# class Person:
#     pclass="mammalia"
#     def __init__(self,name):
#         self.name=name
# p=Person("jajay")
# print(Person.pclass)

#
#
#
# #exception
#
# #error
# #exception
# #exception handling
lst=[1,2,3]
no1=int(input("enter value for no1"))
no2=int(input("enter value for no2"))
try:
    res=no1/no2#10/2
    print(res)#5

except Exception as e:
    print(e.args)
try:
    print(lst[5])
except Exception as e:
    print(e.args)
print("i have one database transaction")
print("i have one file transaction")

#
# #try:
# #doubtful code
# #except:
# #exception handling code

