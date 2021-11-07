def isleap(y):
    if(y%4==0):
        if(y%100==0 and y%400!=0):
            return 0
        else:
            return 1
    else:
        return 0
        
year = int(input())
if(isleap(year)):
    print("Its leap Year.")
else:
    print("Its not a leap year.")