#!/usr/bin/python3

from math import sin, log, exp, pi
from utilities import NormBinSeqToNum

def MaxMinEval(individual):
    negInd=list(map(int,[not i for i in list(map(bool,individual))]))
    return max( (sum(individual)) , (sum(negInd)) ),

def OneMaxEval(individual):
    return sum(individual),

def FnctA(individual):
    x=NormBinSeqToNum(individual)
    return ( sin( 5*pi*( (x)**(3/4) - 0.05 ) ) )**6,

def FnctB(individual):
    x=NormBinSeqToNum(individual)
    return ( exp( -2*(log(2))*(( (x-0.08)/(0.834) )**2) ) )*( FnctA(individual)[0] ),