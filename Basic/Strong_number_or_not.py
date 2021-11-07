def factorial(sum, num):
    if num<0:
        return 0
    if num==0:
        return 1
    if num==1:
        return sum
    return factorial(sum*num, num-1)

n = int(input())
temp = n
summ = 0
while(n>=1):
    summ += factorial(1, int(n%10))
    n/=10
print(summ, temp)

if(temp==summ):
    print("Strong Number")
else: 
    print("Not a Strong Number")