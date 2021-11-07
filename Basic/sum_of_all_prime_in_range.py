def isprime(n):
    if(n<2):
        return 0
    for i in range(2, n):
        if(n%i==0):
            return 0
    return 1

# num = int(input())
a = int(input())
b = int(input())
sum = 0
for i in range(a, b):
    if(isprime(i)):
        sum += i
    else:
        print("Its not a prime number")
print(sum)