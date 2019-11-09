#!/usr/bin/python3

import random
from deap import creator, base, tools, algorithms
import matplotlib.pyplot as plt
import itertools

def GenBinSeq(k):
    return [list(map(int,x)) for x in itertools.product('01', repeat=k)]

def BinSeqToNum(BinSeq):
    return int("".join([str(i) for i in BinSeq]), 2)

def NormBinSeqToNum(BinSeq):
    return (BinSeqToNum(BinSeq)/(2**len(BinSeq)-1))

def PlotBinSeq(BinSeq, FitValue, PlotProperty='b-'):
    xaxis=[ "".join([(str(i)) for i in j]) for j in BinSeq]
    plt.plot(xaxis,FitValue, str(PlotProperty))
    return plt

def PlotBinFct(BinSeq, FitFunction, PlotProperty='b-'):
    yaxis=[FitFunction(i)[0] for i in BinSeq]  # evaluate the FitFunction
    xaxis=[ "".join([(str(i)) for i in j]) for j in BinSeq]
    plt.plot(xaxis,yaxis, str(PlotProperty))
    return plt

def ScatBinSeq(BinSeq, FitValue):
    xaxis=[ "".join([(str(i)) for i in j]) for j in BinSeq]
    plt.scatter(xaxis,FitValue)
    return plt

def ScatBinFct(BinSeq, FitFunction):
    yaxis=[FitFunction(i)[0] for i in BinSeq]  # evaluate the FitFunction
    xaxis=[ "".join([(str(i)) for i in j]) for j in BinSeq]
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