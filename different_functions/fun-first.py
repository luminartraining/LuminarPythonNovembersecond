# def add(num1,num2):
#     res=num1+num2
#     print(res)
# add(10,20)

# variable length argument methods

# def add(*args):
#     sum=0
#     for n in num:
#         sum=sum+n
#     print(sum)
#
#
# add(10,20,30,40,50,60)



def print_data(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
print_data(birth_place="kochi",desig="devop",salary=25000,wrk="aluva")

