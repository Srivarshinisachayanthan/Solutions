s = input().upper()
count = 0

temp = [chr(j) for j in range(65,91)]
l = []
for i in range(2):
    for j in temp:
        l.append(j)

for i in range(len(s)-1):
    
    a = s[i]
    b = s[i+1]
    
    c = abs( l.index(a) - l.index(b) )%26
    if(a<b):
        ii = l.index(a)
        jj = s[i]
    else:
        ii = l.index(b)
        jj = s[i+1]  
    l[ii] = 'a'
    d = abs( l.index(a) - l.index(b) )%26
    l[ii] = jj

    print(l)
    print(c,d,sep="  ")
    
    if(c<d):
        count += c
    else:
        count += d

print(count)
