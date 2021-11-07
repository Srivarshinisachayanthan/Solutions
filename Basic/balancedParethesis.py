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
        print(self.stack)
        # print(" ".join(x for x in self.stack))
        # print(" ".join(self.stack[i] for i in range(len(self.stack))))
        # print(" ".join(self.stack[i] for i in range(len(self.stack)-1, -1, -1)))
        # print(" ".join(item for item in self.stack[::-1]))
        # print(", ".join(item for item in self.stack[::-1]))

if __name__ == "__main__":
    p = input()
    s = Stack()
    for i in p:
        if i in '{[(':
            s.push(i)
        elif i in ')' and s.peek() == '(':
            s.pop()
        elif i in ']' and s.peek() == '[':
            s.pop()
        elif i in '}' and s.peek() == '{':
            s.pop() 
        else:
            break
    if s.isEmpty():
        print("Balanced Parethesis")
    else:
        print("Its not a Balanced Parethesis")
