#function with arg and return value

def add(num1,num2):
    res=num1+num2#60
    return res

def evenChk(num1):
    if(num1%2==0):
        return "even"
    else:
        return "odd"
data=add(10,50)
print(evenChk(data))
