#!/usr/bin/python3

import random
from deap import creator, base, tools, algorithms
import matplotlib.pyplot as plt
import itertools

def binseq(k):
    return [list(map(int,x)) for x in itertools.product('01', repeat=k)]

def MaxEval(individual):
    negInd=list(map(int,[not i for i in list(map(bool,individual))]))
    return max( (sum(individual)) , (sum(negInd)) ) 

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

# define Individual size
IND_SIZE = 6
# define the population size
NUM_IND = 8

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

population = toolbox.population(n=NUM_IND)

plt.subplot(121)
plotBinSeq(binseq(6), MaxEval, 'r')
ScatBinSeq(population, MaxEval)

plt.subplot(122)
BarBinSeq(binseq(6), MaxEval)
BarBinSeq(population, MaxEval)

plt.show()
