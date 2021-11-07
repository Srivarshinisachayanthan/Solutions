number_of_input = int(input())
l = []
for i in range(number_of_input):
    l.append(int(input()))
temp = [i for i in l]
m = max(l)
lo = min(l)
for i in range(number_of_input):
    if l[i]==m:
        l[i] = lo 
print(max(l))