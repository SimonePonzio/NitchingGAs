#!/usr/bin/python3

def FitSharing(individual, pop, fitFunction, distanceFunction, sigma=0.2, shape=1, scaling=1):
    niche = 0
    fit = fitFunction(individual)
    for others in pop:
        dist = distanceFunction(individual, others)
        if dist < sigma:
            niche = niche + ( 1 - (dist/sigma)**shape )
    return((fit[0]**scaling)/niche),
