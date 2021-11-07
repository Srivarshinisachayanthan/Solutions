Node = []
for i in range(int(input())):
    Node.append(map(str, input().split(" ")))

edges={}
for start, end in Node:
    if start in edges:
        edges[start].append(end)
    else:
        edges[start] = [end]

print("\n",Node,sep="",end="\n\n") 
print(edges)