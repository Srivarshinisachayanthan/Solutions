def binary_to_octal(bnum):
    onum = int(bnum, 2)
    onum = oct(onum)
    return onum[2:]

print(binary_to_octal(input()))
