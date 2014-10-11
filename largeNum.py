# suppose you have a very large number, how to numerically represent it
# idea: map str(largeNum) to binary, 4byte for each digit

def storeLargeNum(numStr):
    res = []
    for s in numStr:
       res.append(dec2binary(int(s)))
    return res

def dec2binary(dec):
    if dec==0:
        return 0
    res = ''
    while dec>0:
        res = str(dec%2)+res
        dec //= 2
    return int(res)             

storeLargeNum("12345678901234567890123456789012345678901234567890")
