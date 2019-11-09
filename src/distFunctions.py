#!/usr/bin/python3

# return the normalize hamming distance
def NormHamming2(x,y):
    assert len(x) == len(y)
    count = 0
    for i in range(len(x)):
        if x[i]^y[i]:
            count=count+1
    return float(count)/float(len(x))