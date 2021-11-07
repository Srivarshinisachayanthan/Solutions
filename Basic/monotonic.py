# check the given string is a monotonic.
# Given an array A containing number(n) of integers. The task is to find whether the array is monotonic or not.
# An Array is a monotonic either it is a monotone increasing or monotone decreasing.
# All intergers should be in either assending or a descending is consider as montonic.
# OUTPUT : return "TRUE" if the array is monotonic or else return "False" if its not.


# Solution in python by SACHAYANTHAN_V_2369 


def monotonic(a):
    ascending = True
    descending = True 
    for i in range(len(a)-1):
        if a[i] <= a[i+1]:
            continue
        else:
            ascending = False
            break 
    
    for i in range(len(a)-1):
        if a[i] >= a[i+1]:
            continue
        else:
            descending = False
            break 
            
    if ascending or descending: 
        return True
    return False


if __name__ == "__main__":
    a = list(map(int, input().split(" ")))
    print(monotonic(a))
    