def ispalinum(n):
    for i in range(len(n)):
        if(n[i]!=n[len(n)-i-1]):
            return 0
    return 1

num = int(input())
a = str(num)
if(ispalinum(a)):
    print("Its a palindrome number")
else:
    print("Its not a palindrome number")