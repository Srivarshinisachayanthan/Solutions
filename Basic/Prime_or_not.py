def isprime(n):
    if(n<2):
        return 0
    for i in range(2, n):
        if(n%i==0):
            return 0
    return 1

num = int(input())
if(isprime(num)):
    print("Prime Number")
else:
    print("Its not a prime number")
