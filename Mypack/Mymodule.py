



def sub_dec(func):
    def wrap(no1,no2):
        if no1 < no2:
            no1,no2 = no2, no1
        return func(no1,no2)
    return wrap



def sub(num1,num2):

    return num1-num2


res=sub(40,50)
print(res)


#design patterns

#1mysql
#2:stack

#ORM
#object Relational Mapper
#st=Student(rol=100,name="ajay",total=150)
# st.save()
#











#div
#div(2,5)
@sub_dec
def div(num1,num2):
    return num1/num2
data=div(2,10)
print(data)