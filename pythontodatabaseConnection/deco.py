
def smart_sub(func):
    def wrappe(num1,num2):
        if num1<num2:
            num1,num2=num2,num1
        return func(num1,num2)
    return wrappe
@smart_sub
def sub(num1,num2):
    res=num1-num2
    print(res)
sub(10,20)