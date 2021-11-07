# INPUT : 1 <= 1015. Find the largest Prime Factor of a number.
# For example, if the input number is 12, then output should be "2 2 3". Then output should be 3.
# If the input number is 315, then output should be "3 3 5 7". then ouput should be 7.
# If the input number is 10, then output should be "2 5". then ouput should be 5.

def isprime(n):
    if(n<2):
        return 0
    for i in range(2, n):
        if(n%i==0):
            return 0
    return 1

if __name__ == "__main__":
    num = int(input())
    p = 2
    l = []
    while(num>2):
        if isprime(p):
            if num%p==0:
                l.append(p)
                num/=p 
                
            else:
                p+=1
        else:
            p+=1
    print(max(l))