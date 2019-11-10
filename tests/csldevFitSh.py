#!/usr/bin/python3

import random
from deap import creator, base, tools, algorithms
from utilities import NormBinSeqToNum, PlotBinSeq, ScatBinFct, GenBinSeq
import matplotlib.pyplot as plt
from NichingMethods import FitSharing
from distFunctions import NormHamming2, NichCluster
from statistics import mean
from FitFunctions import MaxMinEval, FnctA, FnctB, MaxFnctA, MaxFnctB
from benchmark import MaxPeakRatio, ChiSquareLike

# define Individual size
IND_SIZE = 12
# define num of individual
NUM_IND = 100
# define max num of generations
MAX_NUM_GEN = 50
# define the fitness function [FnctA, FnctB]
FitnessFunction = FnctA
# define the corresponding set of PeackValues [MaxFnctA, MaxFnctB]
PeackValues = MaxFnctA

creator.create("FitnShare", base.Fitness, weights=(1.0,))
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax, fitshare=creator.FitnShare, value=0)

toolbox = base.Toolbox()

toolbox.register("evalfit", FitnessFunction)
toolbox.register("evalfitsh", FitSharing, fitFunction=toolbox.evalfit, distanceFunction=NormHamming2, sigma=0.2)
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
# toolbox.register("select", tools.selStochasticUniversalSampling, fit_attr='fitshare')
toolbox.register("select", tools.selTournament, tournsize=5, fit_attr='fitshare')

rapresentative=toolbox.population(n=len(PeackValues))
for ind,rap in zip(rapresentative,PeackValues):
    ind.value=rap[0]
    ind.fitness=rap[1]

csq_dev=[]

for num_gen in range(MAX_NUM_GEN):

    population = toolbox.population(n=NUM_IND)
    
    for gen in range(num_gen):
        offspring = algorithms.varAnd(population, toolbox, cxpb=0.1, mutpb=0.01)
        for ind in offspring:
            ind.fitshare.values = toolbox.evalfitsh(ind, offspring)
        population = toolbox.select(offspring, k=len(population))

        for ind in population:
            ind.value=NormBinSeqToNum(ind)
            ind.fitness.values=toolbox.evalfit(ind)

    csq_dev.append(ChiSquareLike(population, rapresentative, nich_radius=0.1))

plt.plot([i for i in range(MAX_NUM_GEN)],csq_dev)
plt.title('generation VS ChiSquareLike')
plt.xlabel('generation')
plt.ylabel('ChiSquareLike')
plt.show()
