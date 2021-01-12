class Books:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return Books(self.pages+other.pages) # 100+200=300
    def __str__(self):
        return str(self.pages)



obj=Books(100)

obj1=Books(200)
obj2=Books(300)
print(obj+obj1) #
print(obj+obj1+obj2)#+obj2 books+books
