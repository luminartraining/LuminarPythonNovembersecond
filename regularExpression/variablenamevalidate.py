#variable name rule
#strating with a-k
#second charater shouldbe a digit and it mustbe divisible by 3
#follwed by any number of characters
# z2rggg =>invalid
#B7vggg=>invalid
#a3rgggg=>valid
from re import *

rule='[a-kA-K][369][a-zA-Z0-9]'

variblename=input("enter valriable name")

matcher=fullmatch(rule,variblename)
if matcher !=None:
    print("valid variable name")
else:
    print("invalid")
