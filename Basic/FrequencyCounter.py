from collections import Counter

a="SriVarShiniSachaYanThan Lovers And CoupLes Forever".lower()
ans=Counter(a)
c=Counter()
print(c[a])
for i in 'abcdefghijklmnopqrstuvwxyz':
    if i in a:
        print(i,ans[i])
