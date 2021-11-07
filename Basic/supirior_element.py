def supirior(l, n):
    count = 0
    for i in range(n):
        ok = 1
        for j in range(i+1, n):
            if(l[i]<=l[j]):
                ok = 0
        if ok==1:
            count += 1
    return count

if __name__ == "__main__":
    n = int(input())
    l = []
    for i in range(n):
        l.append(int(input()))
    a = supirior(l, n)
    print("\n",a)