#
size=int(input("enter the size of stack"))
stk=[]

top=0
n=1
def push(element):

    global top

  if(top>=size):
      print("stack is full")
  else:
      stk.append(element)
      top+=1

def pop():
    print("pop...")
def display():
    print("display")
while(n!=0):
    option=int(input("enter operation u want to perform 1)push 2)pop 3)display"))
    if(option==1):
        elemnt=input()
        push(elemnt)
    elif(option==2):
        pop()
    elif option==3:
        display()
    else:
        print("invalid option")
    n=int(input("enter do u want to continue press 0 for exit"))

