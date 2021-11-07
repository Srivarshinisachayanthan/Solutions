l = sorted(list(map(int, input().split(" "))))
l = sorted(l)
print(l)
s = 0
ll = int(len(l))
for i in range(int(ll/2)):
    m = l[i] + l[ll-1-i]
    print(i,ll-i-1,l[i],l[ll-1-i],sep=" - ",end="")
    print("M-",m,"S-",s,sep="")
    if s < m:
        s = m
print(s)
