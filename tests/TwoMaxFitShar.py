#!/usr/bin/python3

import random
from deap import creator, base, tools, algorithms
from utilities import BarBinFct, BarBinSeq, GenBinSeq
import matplotlib.pyplot as plt
from NitchingMethods import FitSharing
from distFunctions import NormHamming2
from FitFunctions import MaxMinEval

# define Individual size
IND_SIZE = 10
# define num of individual
NUM_IND = 200
# define num of generations
NUM_GEN = 3

creator.create("FitnShare", base.Fitness, weights=(1.0,))
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax, fitshare=creator.FitnShare)

toolbox = base.Toolbox()

toolbox.register("evalfit", MaxMinEval)
toolbox.register("evalfitsh", FitSharing, fitFunction=toolbox.evalfit, distanceFunction=NormHamming2)
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3, fit_attr='fitshare')

population = toolbox.population(n=NUM_IND)

AllBinSeq = GenBinSeq(IND_SIZE)
AllPossibleFits = [MaxMinEval(i)[0] for i in AllBinSeq]

for gen in range(NUM_GEN):
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
    for ind in offspring:
        ind.fitshare.values = toolbox.evalfitsh(ind, offspring)
    population = toolbox.select(offspring, k=len(population))

    BarBinSeq(AllBinSeq, AllPossibleFits)
    BarBinSeq(population, [MaxMinEval(i)[0] for i in population])
    plt.show()

for ind in population:
    ind.fitness.values = toolbox.evalfit(ind)
top3 = tools.selBest(population, k=3, fit_attr='fitness')
print(top3)