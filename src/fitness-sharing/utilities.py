#!/usr/bin/python3

import random
from deap import creator, base, tools, algorithms
import matplotlib.pyplot as plt
import itertools

def binseq(k):
    return [list(map(int,x)) for x in itertools.product('01', repeat=k)]

def plotBinSeq(BinSeq, FitFunction, PlotProperty):
    yaxis=[FitFunction(i) for i in BinSeq]  # evaluate the FitFunction
    xaxis=[ "".join([(str(i)) for i in j]) for j in BinSeq]
    plt.plot(xaxis,yaxis, str(PlotProperty))
    plt.grid(True)
    return plt

def ScatBinSeq(BinSeq, FitFunction):
    yaxis=[FitFunction(i) for i in BinSeq]  # evaluate the FitFunction
    xaxis=[ "".join([(str(i)) for i in j]) for j in BinSeq]
    plt.scatter(xaxis,yaxis)
    plt.grid(True)
    return plt

def BarBinSeq(BinSeq, FitFunction):
    yaxis=[FitFunction(i) for i in BinSeq]  # evaluate the FitFunction
    xaxis=[ "".join([(str(i)) for i in j]) for j in BinSeq]
    plt.grid(True)
    plt.bar(xaxis,yaxis)
    return plt