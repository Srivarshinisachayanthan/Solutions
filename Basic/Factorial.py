def factorial(sum, num):
    if num<0:
        return 0
    if num==0:
        return 1
    if num==1:
        return sum
    return factorial(sum*num, num-1)
 
n = int(input())
print(factorial(1, n))