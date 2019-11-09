#!/usr/bin/python3

import random
from deap import creator, base, tools, algorithms
from utilities import BarBinFct, BarBinSeq, GenBinSeq
import matplotlib.pyplot as plt
from FitFunctions import MaxMinEval

# define Individual size
IND_SIZE = 10
# define num of individual
NUM_IND = 100
# define num of generations
NUM_GEN = 3

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", MaxMinEval)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

population = toolbox.population(n=NUM_IND)

AllBinSeq = GenBinSeq(IND_SIZE)
AllPossibleFits = [MaxMinEval(i)[0] for i in AllBinSeq]

for gen in range(NUM_GEN):
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
    fits = toolbox.map(toolbox.evaluate, offspring)
    for fit, ind in zip(fits, offspring):
        ind.fitness.values = fit
    population = toolbox.select(offspring, k=len(population))

    BarBinSeq(AllBinSeq, AllPossibleFits)
    BarBinSeq(population, [x.fitness.values[0] for x in population])
    plt.show()

top10 = tools.selBest(population, k=3)
print(top10)