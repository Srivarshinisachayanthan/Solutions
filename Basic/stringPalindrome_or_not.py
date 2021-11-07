def ispali(n):
    for i in range(len(n)):
        if(n[i]!=n[len(n)-i-1]):
            return 0
    return 1

s = input()
if(ispali(s)):
    print("Its a palindrome string")
else:
    print("Its not a palindrome string")