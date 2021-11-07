class Book:
    def _init_(self,id, name, author, typ, price):
        self.id = id 
        self.name = name 
        self.author = author 
        self.typ = typ 
        self.price = price 


class bookstore:
    def __init__(self,booklist):
        self.booklist = booklist
        
    def dis(self, name):
        for i in self.booklist:
            if i.name == name:
                if i.author > 4: 
                    return [i.typ, i.price(20/100) ]
                    i.price = i.price(20/100)
                else:
                    return [i.typ, i.price(10/100) ]
                    i.price = i.price(10/100)
        return None 

    def depict(self, p):
        count=0
        for i in self.booklist:
            if i.price == p:
                count+=1
        return count 

if __name__ =="__main__":
    testcase = int(input())
    l = []
    for i in range(testcase):
        id = int(input())
        name = input()
        author = input()
        typ = input()
        price = int(input())
        l.append(Book(id, name, author, typ, price))
    
n = input()
obj = bookstore(l)
print(obj.dis(n))
print(obj.depict(int(input())))
