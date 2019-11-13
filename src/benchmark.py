#!/usr/bin/python3

from distFunctions import FloatDist, BestMatch, NichCluster
from math import sqrt

def MaxPeakRatio(population, real_opt, dist_funct=FloatDist, sigma=0.1, fit_match=0.8, pos_attr="value"):
    num=0
    for vip in real_opt:
        best_ind = BestMatch(population, vip, dist_funct, pos_attr=pos_attr)
        if (dist_funct(getattr(vip,pos_attr),getattr(best_ind,pos_attr))<sigma and best_ind.fitness.values[0]/vip.fitness>fit_match):
             num=num+best_ind.fitness.values[0]
    den=sum([ vip.fitness for vip in real_opt ])
    return num/den

#getattr(vip,pos_attr)  #getattr(best_ind,pos_attr)

def ChiSquareLike(population, real_opt, nich_radius=0.1, dist_funct=FloatDist, fitness="fitness", attr_value="value"):
    """
    population is a list of individuals to evaluate.
    real_opt is the list of the real best individuals.
    each indiviadual has attributes [for istance: value, fitness, ecc..] 
    """
    actual_distr=[len(nich) for nich in NichCluster(population, real_opt, dist_funct=dist_funct, attr_value=attr_value)]
    real_opt_fit_sum=sum([getattr(i, fitness) for i in real_opt])
    poplen=len(population)
    last_sigma=0
    csl_square=0

    for adi,idx in zip(actual_distr, range(len(actual_distr))):
        if idx<len(real_opt):
            mid=poplen*getattr(real_opt[idx],fitness)/real_opt_fit_sum # mid = mean ideal distribution
            sigma=mid*(1-(mid/poplen))
            last_sigma=last_sigma+(sigma**2)
        else:
            mid=0
            sigma=last_sigma
    
        csl_square=csl_square+( ((adi-mid)/(sigma**2))**2 )

    return sqrt(csl_square)