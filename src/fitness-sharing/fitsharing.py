#!/usr/bin/python3

def FitSharing(individual, pop, fitFunction, distanceFunction):
    sigma = 0.5
    alpha = 1
    nitche = 0
    fit = fitFunction(individual)
    for others in pop:
        dist = distanceFunction(individual, others)
        if dist < sigma:
            nitche = nitche + ( 1 - (dist/sigma)**alpha )
    return(fit[0]/nitche),
    
# define the distance function as hamming distance
def NormHamming2(x,y):
    assert len(x) == len(y)
    count = 0
    for i in range(len(x)):
        if x[i]^y[i]:
            count=count+1
    return float(count)/float(len(x))