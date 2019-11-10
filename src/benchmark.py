#!/usr/bin/python3

from distFunctions import FloatDist, BestMatch, NitchCluster
from math import sqrt

def MaxPeakRatio(population, real_opt, dist_funct=FloatDist, sigma=0.1, fit_match=0.8):
    num=0
    for vip in real_opt:
        best_ind = BestMatch(population, vip, dist_funct)
        if (dist_funct(vip[0],best_ind[0])<sigma and best_ind[1]/vip[1]>fit_match):
             num=num+best_ind[1]
    den=sum([ vip[1] for vip in real_opt ])
    return num/den


def ChiSquareLike(population, real_opt, nitch_radius=0.1, dist_funct=FloatDist, fitness="fitness", attr_value="value"):
    """
    population is a list of individuals
    real_opt is a list of individuals and has an attribute 'fitness'
    """
    actual_distr=[len(nitch) for nitch in NitchCluster(population, real_opt, dist_funct=dist_funct, attr_value=attr_value)]
    real_opt_fit_sum=sum([getattr(i, fitness) for i in real_opt])
    poplen=len(population)
    last_sigma=0
    csl_square=0

    for adi,idx in zip(actual_distr, range(len(actual_distr))):
        if idx<len(real_opt):
            mid=poplen*getattr(real_opt[idx],fitness)/real_opt_fit_sum # mid = mean ideal distribution
            sigma=mid*(1-(mid/poplen))
            last_sigma=last_sigma+sigma
        else:
            mid=0
            sigma=last_sigma
    
        csl_square=csl_square+( ((adi-mid)/sigma)**2 )

    return sqrt(csl_square)