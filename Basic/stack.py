from sys import maxsize

def createstack():
    stack = []
    return stack

def isempty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if isempty(stack):
        return str(-maxsize -1)
    return stack.pop()

def peek(stack):
    if isempty(stack):
        return str(-maxsize - 1)
    return stack[len(stack)-1]

def printstack(stack):
    for i in stack[::-1]:
        print(i,"|---------------------|",sep="\n")

print("\n\n")
stack = createstack() 
push(stack, str(5))
push(stack, str(50))
push(stack, str(500))
push(stack, str(5000))
push(stack, str(50000))
push(stack, str(500000))
printstack(stack)
print("\n\n")
pop(stack)
printstack(stack)
print("\n\n")
pop(stack)
printstack(stack)
print("\n\n")
pop(stack)
printstack(stack)
print("\n\n")
pop(stack)
printstack(stack)
print("\n\n")
pop(stack)
printstack(stack)
print("\n\n")
print(pop(stack))
printstack(stack)
print("\n\n")
print(pop(stack))
printstack(stack)
print("\n\n")