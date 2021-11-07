# Assume that the product codes of the items are 101, 103, 101, 102, 104
# Repeated product code is the quantitu of that item. According to
# the above series we can find the stock of the items 
# 
# product code      Item Quantity
# 101               2    
# 103               2
# 102               1
# 104               1
# 
# In that case, both 102 and 104 are only one quantity, but first 
# occurance is 102. So, The answer must be 2.
# In case the none of the quantity is 1 [All greater than 1].
# Then print "No Out Of Stock".

# Inputs, n - number of inputs, then next lines n no. of inputs given by id

if __name__ == "__main__":
    n = int(input())
    l = dict()
    for i in range(n):
        k = input()
        v = 1
        try: 
            l.update({k: l[k] + v })
        except:
            l[k] = v
    for k,v in l.items():
        if v==1:
            print(k)
            break
            