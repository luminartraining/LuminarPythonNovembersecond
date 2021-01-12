#bank
#create_account()
#deposit()
#witdraw()
#balance_enq()
import datetime

class Bank:
    bank_name="sbk"
    def __init__(self,acno,person_name,balance):
        self.acno=acno
        self.person_name=person_name
        self.balance=balance


    def deposit(self,amount):
        self.balance+=amount
        print(Bank.bank_name,"you account ",self.acno,"has been crerdited with amount",amount,datetime.date.today(),"you aval balance",self.balance)

    def withdraw(self,amount):
        if(amount>self.balance):
            print("insufficient amount in your account trasaction failed")
        else:
            self.balance-=amount
            print("you account ", self.acno, "has been debited with amount", amount, "you aval balance", self.balance)

    def balance_enq(self):
        print("your current account balance=",self.balance)
    def __str__(self):



obj=Bank(1000,"reji",3000)

obj.deposit(5000)
obj.withdraw(25000)

#different types of variables,instance variable,static
#instance variables->

#instance variable are always prepended with self key word

#we can acess instance variables outside class with referncename.instance variable
"""self.acno,self.person_name,self.balance,self.bank_name"""


#static variables/class variables
#efficient memory utilization

#access by using class name.Static variable name