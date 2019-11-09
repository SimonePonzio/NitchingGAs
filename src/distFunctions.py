#!/usr/bin/python3

# return the normalize hamming distance
def NormHamming2(x,y):
    assert len(x) == len(y)
    count = 0
    for i in range(len(x)):
        if x[i]^y[i]:
            count=count+1
    return float(count)/float(len(x))

def FloatDist(x,y):
    return abs(x - y)

def BestMatch(goal_ind, population, dist_funct=FloatDist):
    dist_ind = [(dist_funct(goal_ind[0], individual[0])) for individual in population]
    BestInd = population[dist_ind.index(min(dist_ind))]
    return BestInd