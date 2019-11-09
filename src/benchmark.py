#!/usr/bin/python3

from distFunctions import FloatDist, BestMatch

def MaxPeakRatio(population, real_opt, dist_funct=FloatDist, sigma=0.1, fit_match=0.8):
    num=0
    for vip in real_opt:
        best_ind = BestMatch(vip, population, dist_funct)
        if (dist_funct(vip[0],best_ind[0])<sigma and best_ind[1]/vip[1]>fit_match):
             num=num+best_ind[1]
    den=sum([ vip[1] for vip in real_opt ])
    return num/den
