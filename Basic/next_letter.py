s = input()
in1 = s[0]
in2 = s[2]

if(in1<in2):
    d = abs(ord(in2)-ord(in1)) % 26
    temp = [chr(j) for j in range(97,123)]
    l = []
    for i in range(2):
        for j in temp:
            l.append(j)
    print(l[l.index(in2)+d])
else:
    d = abs(ord(in1)-ord(in2)) % 26
    temp = [chr(j) for j in range(122,96,-1)]
    l = []
    for i in range(2):
        for j in temp:
            l.append(j)
    print(l[l.index(in2)+d])