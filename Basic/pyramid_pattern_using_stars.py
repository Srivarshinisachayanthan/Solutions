# *****
#  ***
#   *
#      *
#     ***
#    *****
#   *******
#  *********
# ***********

n = int(input())
for i in range(n+1):
    for j in range(0, n-i):
        print(" ",sep="",end="")
    for k in range(0,i):
        print('*',sep="",end="")
    for j in range(0,i-1):
        print('*',sep="",end="")
    print()
