class Stack:
    def __init__(self):
        self.len=0
        self.stack = []
            
    def push(self,data):
        self.stack.append(data)
        self.len+=1
    
    def pop(self):
        if self.len==0:
            return -1
        self.len-=1
        return self.stack.pop()
    
    def isEmpty(self):
        return self.len==0
    
    def peek(self):
        if self.len>0:
            return self.stack[self.len - 1]
        return -1
    
    def size(self):
        return self.len 
    
    def display(self):
        print(self.stack[::-1])
    
s = Stack()
s.push(str(5))
s.push(str(10))
s.push(str(15))
s.push(str(20))

print(s.size())
s.display()
print(s.pop())
s.display()
# print(s.peek())
print(s.size())
s.display()
