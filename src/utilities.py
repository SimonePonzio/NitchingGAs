#!/usr/bin/python3

import random
from deap import creator, base, tools, algorithms
import matplotlib.pyplot as plt
import itertools

def GenBinSeq(k):
    return [list(map(int,x)) for x in itertools.product('01', repeat=k)]

def PlotBinSeq(BinSeq, FitValue, PlotProperty='b-'):
    xaxis=[ "".join([(str(i)) for i in j]) for j in BinSeq]
    plt.plot(xaxis,FitValue, str(PlotProperty))
    plt.grid(True)
    return plt

def PlotBinFct(BinSeq, FitFunction, PlotProperty='b-'):
    yaxis=[FitFunction(i)[0] for i in BinSeq]  # evaluate the FitFunction
    xaxis=[ "".join([(str(i)) for i in j]) for j in BinSeq]
    plt.plot(xaxis,yaxis, str(PlotProperty))
    plt.grid(True)
    return plt

def ScatBinSeq(BinSeq, FitValue):
    xaxis=[ "".join([(str(i)) for i in j]) for j in BinSeq]
    plt.scatter(xaxis,FitValue)
    plt.grid(True)
    return plt

def ScatBinFct(BinSeq, FitFunction):
    yaxis=[FitFunction(i)[0] for i in BinSeq]  # evaluate the FitFunction
    xaxis=[ "".join([(str(i)) for i in j]) for j in BinSeq]
    plt.scatter(xaxis,yaxis)
    plt.grid(True)
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