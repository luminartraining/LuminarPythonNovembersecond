pattern="ABABAC"
dict={}
for char in pattern:#a b
    if char not in dict:#
        dict[char]=1#a:1,b:1
    else:
        print("recursive character is",char)
        break