#!/usr/bin/python3

import random
from deap import creator, base, tools, algorithms
import matplotlib.pyplot as plt
import itertools

def GenBinSeq(k):
    return [list(map(int,x)) for x in itertools.product('01', repeat=k)]

def BinSeqToNum(BinSeq):
    return int("".join([str(i) for i in BinSeq]), 2)

def NormBinSeqToNum(BinSeq, base=1):
    return ((BinSeqToNum(BinSeq)*base)/(2**len(BinSeq)-1))

# split the binary sequence in n same size chunks
def SplitBinSeq(BinSeq, numchunks):
    lenseq=len(BinSeq)
    lenchunk=0
    if lenseq%numchunks==0:
        lenchunk=int(lenseq/numchunks)
    else:
        carry=lenseq%numchunks
        lenchunk=int((lenseq-carry)/numchunks)
    return [BinSeq[i:i+lenchunk] for i in range(0, lenseq, lenchunk)]

def PlotBinSeq(BinSeq, FitValue, PlotProperty='b-'):
    xaxis=[NormBinSeqToNum(i) for i in BinSeq]
    # xaxis=[ "".join([(str(i)) for i in j]) for j in BinSeq]
    plt.plot(xaxis,FitValue, str(PlotProperty))
    return plt

def PlotBinFct(BinSeq, FitFunction, PlotProperty='b-'):
    yaxis=[FitFunction(i)[0] for i in BinSeq]  # evaluate the FitFunction
    xaxis=[NormBinSeqToNum(i) for i in BinSeq]
    plt.plot(xaxis,yaxis, str(PlotProperty))
    return plt

def ScatBinSeq(BinSeq, FitValue):
    xaxis=[ "".join([(str(i)) for i in j]) for j in BinSeq]
    plt.scatter(xaxis,FitValue)
    return plt

def ScatBinFct(BinSeq, FitFunction):
    yaxis=[FitFunction(i)[0] for i in BinSeq]  # evaluate the FitFunction
    xaxis=[NormBinSeqToNum(i) for i in BinSeq]
    plt.scatter(xaxis,yaxis)
    return plt
    
def BarBinFct(BinSeq, FitFunction):
    yaxis=[FitFunction(i)[0] for i in BinSeq]  # evaluate the FitFunction
    xaxis=[ "".join([(str(i)) for i in j]) for j in BinSeq]
    plt.bar(xaxis,yaxis)
    return plt

def BarBinSeq(BinSeq, FitValue):
    # yaxis=[FitFunction(i) for i in BinSeq]  # evaluate the FitFunction
    xaxis=[ "".join([(str(i)) for i in j]) for j in BinSeq]
    plt.bar(xaxis,FitValue)
    return plt