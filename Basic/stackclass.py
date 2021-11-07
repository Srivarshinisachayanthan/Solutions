from sys import maxsize


class Stack:
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        return len(self.stack) == 0
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if self.isEmpty():
            return str(-maxsize - 1)
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return str(-maxsize - 1)
        return self.stack[len(self.stack) - 1]
    def size(self):
        return len(self.stack)
    def display(self):
        print(" ".join(x for x in self.stack))
        print(" ".join(self.stack[i] for i in range(len(self.stack))))
        print(" ".join(self.stack[i] for i in range(len(self.stack)-1, -1, -1)))
        print(" ".join(item for item in self.stack[::-1]))
        print(", ".join(item for item in self.stack[::-1]))

s = Stack()
s.push(str(5))
s.push(str(10))
s.push(str(15))
s.push(str(20))
print(s.pop())
print(s.peek())
print(s.size())
s.display()