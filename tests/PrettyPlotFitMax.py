#!/usr/bin/python3

import random
from deap import creator, base, tools, algorithms
from utilities import PlotBinSeq, ScatBinFct, GenBinSeq
import matplotlib.pyplot as plt
from FitFunctions import MaxMinEval, FnctA, FnctB

# define Individual size
IND_SIZE = 12
# define num of individual
NUM_IND = 100
# define num of generations
NUM_GEN = 50
# define the fitness function between [FnctA, FnctB]
FitnessFunction = FnctA

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", FitnessFunction)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

population = toolbox.population(n=NUM_IND)

AllBinSeq = GenBinSeq(IND_SIZE)
AllPossibleFits = [FitnessFunction(i)[0] for i in AllBinSeq]

for gen in range(NUM_GEN):
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
    fits = toolbox.map(toolbox.evaluate, offspring)
    for fit, ind in zip(fits, offspring):
        ind.fitness.values = fit
    population = toolbox.select(offspring, k=len(population))

PlotBinSeq(AllBinSeq, AllPossibleFits, 'r')
ScatBinFct(population, FitnessFunction)
plt.show()

for ind in population:
    ind.fitness.values = toolbox.evaluate(ind)
top3 = tools.selBest(population, k=3, fit_attr='fitness')
print(top3)