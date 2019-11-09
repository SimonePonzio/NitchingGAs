#!/usr/bin/python3

# MyPop=[ [0.08,1], [0.220,1], [0.451,0.95], [0.670,0.95], [0.9,0.7] ]
# print(MaxPeakRatio(MyPop, MaxFnctA))

#!/usr/bin/python3

import random
from deap import creator, base, tools, algorithms
from utilities import NormBinSeqToNum, PlotBinSeq, ScatBinFct, GenBinSeq
import matplotlib.pyplot as plt
from NitchingMethods import FitSharing
from distFunctions import NormHamming2
from statistics import mean
from FitFunctions import MaxMinEval, FnctA, FnctB, MaxFnctA, MaxFnctB
from benchmark import MaxPeakRatio

# define Individual size
IND_SIZE = 12
# define num of individual
NUM_IND = 100
# define max num of generations
MAX_NUM_GEN = 50
# define the fitness function between [FnctA, FnctB]
FitnessFunction = FnctA

creator.create("FitnShare", base.Fitness, weights=(1.0,))
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax, fitshare=creator.FitnShare)

toolbox = base.Toolbox()

toolbox.register("evalfit", FitnessFunction)
toolbox.register("evalfitsh", FitSharing, fitFunction=toolbox.evalfit, distanceFunction=NormHamming2, sigma=0.2)
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selStochasticUniversalSampling, fit_attr='fitshare')
# toolbox.register("select", tools.selTournament, tournsize=5, fit_attr='fitshare')

BenchMark=[]

for num_gen in range(MAX_NUM_GEN):
    population = toolbox.population(n=NUM_IND)

    for gen in range(num_gen):
        offspring = algorithms.varAnd(population, toolbox, cxpb=0.1, mutpb=0.01)
        for ind in offspring:
            ind.fitshare.values = toolbox.evalfitsh(ind, offspring)
        population = toolbox.select(offspring, k=len(population))

    final_pop=list([ [NormBinSeqToNum(i) ,toolbox.evalfit(i)[0]] for i in population])
    BenchMark.append(MaxPeakRatio(final_pop, MaxFnctA))

plt.scatter([i for i in range(MAX_NUM_GEN)],BenchMark)
plt.show()