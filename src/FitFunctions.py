#!/usr/bin/python3

from math import sin, log, exp, pi
from utilities import NormBinSeqToNum, SplitBinSeq

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

MaxFnctA=[ [0.08,1], [0.247,1], [0.451,1], [0.681,1], [0.934,1] ]
MaxFnctB=[ [0.08,1], [0.247,0.948], [0.451,0.770], [0.681,0.503], [0.934,0.250] ]

def eggcrate(individual):
    coord=SplitBinSeq(individual,2)
    x=NormBinSeqToNum(coord[0],5)
    y=NormBinSeqToNum(coord[1],5)
    return ( x**2 + y**2 + 25*( (sin(x))**2 + (sin(y))**2 ) )

def himmelblau(individual):
    coord=SplitBinSeq(individual,2)
    x=NormBinSeqToNum(coord[0],5)
    y=NormBinSeqToNum(coord[1],5)
    return ( ( x**2 + y - 11 )**2 + ( x + y**2 -7 )**2 )
